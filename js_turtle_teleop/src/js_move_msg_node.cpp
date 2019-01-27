#include "ros/ros.h"  
#include "geometry_msgs/Twist.h"
#include "sensor_msgs/Joy.h" 

class Teleop  
{  
    public:  
        Teleop();
        void pub_twist();

    private:  
        void callback(const sensor_msgs::Joy::ConstPtr& Joy);  
        ros::NodeHandle n;
        ros::Subscriber sub;  
        ros::Publisher pub;  
        double max_lin_speed, max_ang_speed, lin_speed, ang_speed;
        int lin_axis, ang_axis;
};  
  
Teleop::Teleop()  
{
    lin_speed = 0.0;
    ang_speed = 0.0;
    n.param<int>("linear_axis_num", lin_axis, 1);
    n.param<int>("angular_axis_num", ang_axis, 3);
    n.param<double>("max_linear_speed", max_lin_speed, 2.0);
    n.param<double>("max_angular_speed", max_ang_speed, 2.0);
    pub = n.advertise<geometry_msgs::Twist>("/turtle1/cmd_vel", 1);
    sub = n.subscribe<sensor_msgs::Joy>("/joy", 10, &Teleop::callback, this);
}

void Teleop::pub_twist()
{
    geometry_msgs::Twist v;
    v.linear.x = lin_speed;
    v.angular.z = ang_speed;    
    pub.publish(v);  
}

void Teleop::callback(const sensor_msgs::Joy::ConstPtr& Joy)  
{
    lin_speed = Joy -> axes[lin_axis] * max_lin_speed;
    ang_speed = Joy -> axes[ang_axis] * max_ang_speed;  
    ROS_INFO("Turtle speed change: linear:%.3lf angular:%.3lf", lin_speed, ang_speed);   
}  



int main(int argc,char** argv)  
{  
    ros::init(argc, argv, "js_teleop");  
    Teleop teleop;
    ros::Rate loop_rate(50);
    
    while(ros::ok())
    {
        teleop.pub_twist();

        ros::spinOnce();
        loop_rate.sleep();
    }
 
    return 0;  
}  