# deep-vision-4u

A program for manipulating your video streams.

Compose your visual effects and send them to a virtual camera, then open the virtual camera from other programs such as Google Meet.

Enjoy it!

# Project structure

- **deep-vision-4u.py**: script for main application script using the dddpy package
- **dddpy**: package implementing a video processing framework
  - **dddpy-example.py**: script for an example application script using the dddpy package

# Dependencies

## Virtual Camera

To set **output on a virtual camera**, a virtual camera which have to be installed first.

For Windows or MAC install **OBS**, for Linux install **v4l2loopback** (see [pyvirtualcam documentation](https://github.com/letmaik/pyvirtualcam#supported-virtual-cameras)).

## How to Install v4l2loopback on Ubuntu 18.04 LTS

[Reference](https://github.com/umlaeute/v4l2loopback/issues/247)

```bash
wget http://deb.debian.org/debian/pool/main/v/v4l2loopback/v4l2loopback-dkms_0.12.4-1_all.deb

sudo dpkg -i v4l2loopback-dkms_0.12.4-1_all.deb
```

## Create and test a Virtual Camera on Linux

[Reference](https://arcoresearchgroup.wordpress.com/2020/06/02/virtual-camera-for-opencv-using-v4l2loopback/)

```bash
sudo modprobe -r v4l2loopback
sudo modprobe v4l2loopback devices=1 exclusive_caps=1,1 video_nr=5 card_label="deepVision4u Camera"
v4l2-ctl --list-devices -d5
```

to remove virtual cam

```bash
sudo modprobe -r v4l2loopback
```

# Technical Notes

## Managing anaconda environment

[Reference](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)

**Export deep-vision-4u environment in environment.yml**

```bash
conda activate deep-vision-4u
conda env export > environment.yml
```

**Remove deep-vision-4u environment**

```bash
conda remove --name deep-vision-4u --all
```

**Create environment from the environment.yml** and list all environments

```bash
conda env create -f environment.yml
conda env list
```

## Install OpenCV and pyvirtualcam on Ubuntu 18.04 LTS

```
conda activate deep-vision-4u
conda install pip

pip3 install -I opencv-contrib-python
pip3 install pyvirtualcam
```
