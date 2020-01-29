#include "ros/ros.h"
#include "shutter/Shutter.h"
#include <iostream>

class ShutterSlave
{
    public:
        ShutterSlave();

    private:
        int nShutter=2;

        int house = 1;
        int floor = 1;
        int room = 1;

        //2 is nShutter but it gives an compiler error when inserting the variable
        shutter::Shutter shutters[2];

        boost::shared_ptr<shutter::Shutter_<std::allocator<void> > > myCmd;

        void slaveLoop();

        void changeShutterState(int newState, int iShutter=999);

        void cmdCallbackHandle();

        void cmdCallback(shutter::Shutter::Ptr msg);

        //ros sub and pub
        ros::NodeHandle n;

        ros::Subscriber sub_shutter_control;

        ros::Publisher pub_shutter_state;
};

ShutterSlave::ShutterSlave()
{

    sub_shutter_control = n.subscribe("/shutter/cmd", 10 , &ShutterSlave::cmdCallback, this);

    pub_shutter_state = n.advertise<shutter::Shutter>("/shutter/state", 10);

    
    for(int i = 0; i < nShutter; ++i)
    {
        shutters[i].mode = 10;
        shutters[i].house = house;
        shutters[i].floor = floor;
        shutters[i].room = room;
        shutters[i].shutter = i;
        shutters[i].state = 0;
        pub_shutter_state.publish(shutters[i]);
    }

    slaveLoop();
}

void ShutterSlave::slaveLoop()
{
    ros::Rate r(10);
    while(ros::ok())
    {
        //do GPIO handling here


        ros::spinOnce();
        r.sleep();
    }
}

void ShutterSlave::changeShutterState(int newState, int iShutter)
{
    //ROS_INFO("Opening all Shutters");
    if(iShutter==999)
    {
        for(int i = 0; i<nShutter; ++i)
        {
            shutters[i].state=newState;
            pub_shutter_state.publish(shutters[i]);
        }
        if(newState==1)
            ROS_INFO("Opening all Shutters");
        
        else if(newState==-1)
            ROS_INFO("Closing all Shutters");
    }
    else
    {
        if(iShutter<=nShutter)
        {
            shutters[iShutter].state = newState;
            pub_shutter_state.publish(shutters[iShutter]);
            std::cout << "Changed " << iShutter << " to state " << newState << "\n";
        }
        else
        {
            std::cerr << "Shutter not existing, ID is too high";
        }
        
    }

}

void ShutterSlave::cmdCallbackHandle()
{
    //ROS_INFO("Opening Shutter");
    if(myCmd->mode == 1)
    {   
        changeShutterState(myCmd->state);
    }
    else if(myCmd->mode==2)
    {
        if(myCmd->house == house)
        {
            if(myCmd->floor == floor)
            {
                if(myCmd->room == room)
                {
                    if(myCmd->shutter == 99)
                    {
                        changeShutterState(myCmd->state);
                    }
                    else
                    {
                        //open/close specific shutter
                        changeShutterState(myCmd->state, myCmd->shutter);
                    }

                }
                else if(myCmd->room==99)
                {
                    changeShutterState(myCmd->state);
                }
            }
            else if(myCmd->floor==99)
            {
                changeShutterState(myCmd->state);
            }
        }
    }
    else
    {
        ROS_ERROR("Mode is invalid");
    }
    
}

void ShutterSlave::cmdCallback(shutter::Shutter::Ptr msg)
{
    //ROS_INFO("CMD Callback");
    myCmd = std::move(msg);

    cmdCallbackHandle();
}

int main(int argc, char **argv)
{
    ros::init(argc, argv, "shutter_slave");

    ShutterSlave shutter_slave;

    return 0;
}