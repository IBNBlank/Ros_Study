#include <sstream>
#include "ros/ros.h"
#include "ros/this_node.h"
#include "my_message/chat_msg.h"

int main(int argc, char **argv)
{
    ros::init(argc, argv, "talker_cpp");
    ros::NodeHandle nh;
    ros::Publisher pub = nh.advertise<my_message::chat_msg>("chatter", 10);
    ros::Rate loop_rate(2);

    int count = 0;

    while(ros::ok())
    {
        my_message::chat_msg msg;
        std::stringstream ss;

        msg.name = ros::this_node::getName();
        ss << "hello world " << count;
        msg.chat = ss.str();

        ROS_INFO("%s", msg.chat.c_str());
        pub.publish(msg);

        count ++;
        
        ros::spinOnce();
        loop_rate.sleep();
    }

    return 0;
}