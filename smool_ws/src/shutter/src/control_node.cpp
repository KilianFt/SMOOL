#include "ros/ros.h"
#include "std_msgs/String.h"
#include "shutter/Shutter.h"
#include <sstream>
#include <iostream>


class ShutterControl
{
public:
    ShutterControl();
    
private:
    const int cmd_open = 1;
    const int cmd_close = -1;
    const int cmd_neutral = 0;
    const int cmd_all = 1;
    const int cmd_seperate = 2;

    ros::Publisher shutter_pub;
    //ros::Subscriber sub;
    ros::NodeHandle nh;

    void pubTest();
    void shutterLoop();
    void changeShutterState(int state, int mode, int house=0, int floor=0, int room=0, int shutter=0);
    void changeShutterState(shutter::Shutter cmd);
};

ShutterControl::ShutterControl()
{
    shutter_pub = nh.advertise<shutter::Shutter>("shutter/cmd", 1000);

    ShutterControl::shutterLoop();
}

void ShutterControl::changeShutterState(int state, int mode, int house, int floor, int room, int shutterID)
{
    shutter::Shutter cmd;
    cmd.mode = mode;
    cmd.house = house;
    cmd.floor = floor;
    cmd.room = room;
    cmd.shutter = shutterID;
    cmd.state = state;

    shutter_pub.publish(cmd);
}

void ShutterControl::changeShutterState(shutter::Shutter cmd)
{
    //std::cout << "publish" << cmd.house << ", " << cmd.floor << "\n";
    shutter_pub.publish(cmd);
}

void ShutterControl::shutterLoop()
{
    ros::Rate r(10);

    while(ros::ok())
    {
        std::cout << "\n'1' to control all, '2' to control seperate \n";
        int input;
        std::cin >> input;
        std::cin.ignore(32767, '\n');
        if(input==1)
        {
            std::cout << "Controlling all shutters \n'1' to close, '2' to open \n";
            int all_input;
            std::cin >> all_input;
            std::cin.ignore(32767, '\n');
            if(all_input == 1)
            {
                changeShutterState(cmd_close, cmd_all);
                std::cout << "Closing all shutters... \n";
                sleep(2);
                changeShutterState(cmd_neutral, cmd_all);
            }
            else if(all_input == 2)
            {
                std::cout << "Opening all shutters...  \n";
                changeShutterState(cmd_open, cmd_all);
                sleep(2);
                changeShutterState(cmd_neutral, cmd_all);
            }
            else
            {
                std::cerr << "Invalid input \n\n";
            }
        
        }
        else if (input==2)
        {
            std::cerr << "seperate control is not properly working yet \n\n";

            //do seperate shutter handling here
            shutter::Shutter myCMD;
            myCMD.mode = 2;
            std::cout << "BuidingID: \n";
            std::cin >> myCMD.house;
            //std::cout << myCMD.house;
            std::cin.ignore(32767, '\n');
            std::cout << "floorID: \n";
            std::cin >> myCMD.floor;
            std::cin.ignore(32767, '\n');
            //std::cout << myCMD.floor;
            std::cout << "RoomID: \n";
            std::cin >> myCMD.room;
            std::cin.ignore(32767, '\n');
            std::cout << "ShutterID: \n";
            std::cin >> myCMD.shutter;
            std::cin.ignore(32767, '\n');
            std::cout << "'-1' to close, '1' to open: \n";
            std::cin >> myCMD.state;
            std::cin.ignore(32767, '\n');

            changeShutterState(myCMD);
            //changeShutterState(myCMD.state, myCMD.mode, myCMD.house, myCMD.floor, myCMD.room,myCMD.shutter);
            std::cout << "Seperate command published \n";
        }
        else
        {
            std::cerr << "Invalid input \n\n";
        }

        r.sleep();
    }
}

int main(int argc, char **argv)
{
    ros::init(argc, argv, "shutter_control");

    ShutterControl shutter_control;

    ros::spin();
    return 0;
}