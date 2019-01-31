#include "ros/ros.h"
#include "my_message/chat_msg.h"

void callback(const my_message::chat_msg::ConstPtr& msg)
{
    ROS_INFO("I heard [%s] said '%s'", msg -> name.c_str(), msg -> chat.c_str());
}



int main(int argc, char **argv)
{
    ros::init(argc, argv, "listener_cpp");
    ros::NodeHandle nh;
    ros::Subscriber sub = nh.subscribe("chatter", 10, callback);

    ros::spin();

    return 0;
}