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
        ros::NodeHandle nh_;
        ros::Subscriber sub_;
        ros::Publisher pub_;
        double max_lin_speed_, max_ang_speed_, lin_speed_, ang_speed_;
        int lin_axis_, ang_axis_;
};

Teleop::Teleop(): nh_("~"), lin_speed_(0.0), ang_speed_(0.0)
{
    nh_.param<int>("linear_axis_num", lin_axis_, 1);
    nh_.param<int>("angular_axis_num", ang_axis_, 3);
    nh_.param<double>("max_linear_speed", max_lin_speed_, 2.0);
    nh_.param<double>("max_angular_speed", max_ang_speed_, 2.0);
    pub_ = nh_.advertise<geometry_msgs::Twist>("/turtle1/cmd_vel", 1);
    sub_ = nh_.subscribe<sensor_msgs::Joy>("/joy", 10, &Teleop::callback, this);
}

void Teleop::pub_twist()
{
    geometry_msgs::Twist v;
    v.linear.x = lin_speed_;
    v.angular.z = ang_speed_;
    pub_.publish(v);
}

void Teleop::callback(const sensor_msgs::Joy::ConstPtr& Joy)
{
    lin_speed_ = Joy -> axes[lin_axis_] * max_lin_speed_;
    ang_speed_ = Joy -> axes[ang_axis_] * max_ang_speed_;
    ROS_INFO("Turtle speed change: linear:%.3lf angular:%.3lf", lin_speed_, ang_speed_);
}



int main(int argc,char** argv)
{
    ros::init(argc, argv, "js_turtle_teleop_node");
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
