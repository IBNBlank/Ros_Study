#include <ros/ros.h>
#include <image_transport/image_transport.h>
#include <cv_bridge/cv_bridge.h>
#include <sensor_msgs/image_encodings.h>
#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/highgui/highgui.hpp>


class ImageConverter
{
    ros::NodeHandle nh_;
    image_transport::ImageTransport it_;
    image_transport::Subscriber image_sub_;
    image_transport::Publisher image_pub_;


    public:

        ImageConverter(): it_(nh_)
        {
            // Subscrive to input video feed and publish output video feed
            image_sub_ = it_.subscribe("/image_raw", 1, &ImageConverter::imageCb, this);
            image_pub_ = it_.advertise("/image_raw_convert", 1);
        }

        void imageCb(const sensor_msgs::ImageConstPtr& msg)
        {
            cv_bridge::CvImagePtr cv_ptr;
            cv::Mat greyMat;

            // Convert to CV
            cv_ptr = cv_bridge::toCvCopy(msg, sensor_msgs::image_encodings::BGR8);

            // Convert a gray image 
            cv::cvtColor(cv_ptr->image, greyMat, CV_BGR2GRAY); 
            
            // Output modified video stream
            image_pub_.publish(cv_bridge::CvImage(std_msgs::Header(), "mono8", greyMat).toImageMsg());
        }
};



int main(int argc, char** argv)
{
    ros::init(argc, argv, "image_converter");
    ImageConverter ic;
    ros::spin();
    return 0;
}
