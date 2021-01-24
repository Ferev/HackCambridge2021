# Blur

## Inspiration

With the advent of social media users using their platforms to disseminate media, video often must be anonymized before posting in order to preserve the identities of minors, bystanders, and those who do not consent to being filmed in the video. By providing a platform that seamlessly blurs all facial recognition instances, this tool can be seamlessly integrated with any video uploading platform to preserve the actions within it while preserving identity. This provides users the freedom to bring to attention important issues in their community on social media while taking less time and resources to manually edit videos and photos prior to uploading. 

## What it does

This project is a web application that aims to provide robust and quick sensitive information processing in images and videos. After processing a file through ML model, the user is able to download the processed video with blurred faces. 

## How we built it

We split this project into front-end and back-end components. For the back-end component, we leveraged Flask and the PyTorch machine learning pipeline where we used MTCNN to detect faces and then used OpenCV and PIL packages to manipulate the video frames. 

## Challenges we ran into

We initially ran into challenges with multiple edge cases when processing with our ML model. In addition, given the heavy-duty task of processing each frame, we spent a lot of time optimizing our code for it to be as efficient as possible and compromised some quality of the blurs for time performance.

We also experimented with different techniques for image cloaking which essentially aims to apply minor distortions to the image (often irrecognizable by the human eye) as a way to prevent the application of facial recognition models to the video. However due to the computational complexity of some such methods we opted for using facial blurring instead.  

## Accomplishments that we're proud of

We're proud of creating a minimum viable product for an integrated tool for facial blurring. This tool can be used in multiple places, from simple video editing on one's desktop to being a component one can choose if integrated with a social media platform. 

## What we learned

We learned a lot about the PyTorch library, and were able to explore the diverse functionalities and freedom that it provided us. We also learned about contemporary models in computer vision for facial recognition and detection. 

## What's next for Blur

In the future, we hope to incorporate an option to also detect and blur out sensitive information displayed in the video. Beyond just faces, we hope it is able to detect and allow users to manually select other sensitive information, such as house numbers, license plates, mailbox information, etc. 

In addition we would like to explore further techniques for obscuring faces (such as image cloaking) in order to allow our users the option to keep some of the faces on the photo in their original form but still irrecognizable by facial recognition models. In combination with that, we would like to fine tune our face detection model so that we can minimize false positives and false negatives. 
