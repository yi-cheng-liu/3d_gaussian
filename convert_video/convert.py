import cv2
import os
import argparse

def convert_mp4_to_images(input_path, output_folder, stride):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Open the video
    cap = cv2.VideoCapture(input_path)
    frame_count = 0

    while True:
        # Read frame
        ret, frame = cap.read()

        # Check if frame is read correctly
        if not ret:
            break

        # Save frame every 'stride' frames
        if frame_count % stride == 0:
            image_path = os.path.join(output_folder, f"frame_{frame_count}.JPG")
            cv2.imwrite(image_path, frame)

        frame_count += 1

    cap.release()

def main():
    # Argument parser
    parser = argparse.ArgumentParser(description="Convert MP4 video to images with a selected stride.")
    parser.add_argument("--input_path", "-i", help="Path to the MP4 video file")
    parser.add_argument("--output_path", "-o", help="Folder to save the output images")
    parser.add_argument("--stride", "-s", type=int, default=10, help="Stride (interval) for capturing images")

    # Parse arguments
    args = parser.parse_args()

    # Validate file extension
    # if not args.input_path.lower().endswith(('.mp4', '.webm', '.MOV')):
    #     raise ValueError("The video file must be in .mp4 or .webm format")
    
    # Call the function with pqarsed arguments
    convert_mp4_to_images(args.input_path, args.output_path, args.stride)

if __name__ == "__main__":
    main()
