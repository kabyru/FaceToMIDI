# FaceToMIDI

"FaceToMIDI" is a Python project that uses the output of OpenFace's Facial Recognition algorithm as input into PrettyMIDI's music writing capabilities. As you will find by testing different faces, you will notice that the distance the face is from the camera determines the pitch of the song, with each face creating a different variation of a similar melody. This project won't sing you The Beatles, but it will show you that in the eyes of the OpenFace algorithm, faces are relatively similar, with each of us capable of providing different variations to the same tune.

This project requires you to download the OpenFace Windows x64 Release, which can be found [here.](https://github.com/TadasBaltrusaitis/OpenFace/wiki/Windows-Installation) Follow the instructions on the OpenFace installation page to ensure all reference models are properly installed, or this software will not work properly. Simply drop the Release ZIP in the FaceToMIDI directory and extract.

This software makes use of OpenFace 2.0.5 x64 Release. YMMV with other releases, but I recommend that you stick with this release for now, as it is the most recent version made public. The main script searches for an OpenFace 2.0.5 release and will require slight modification to work with other versions.

## How It Works

FaceToMIDI takes a .jpg or .jpeg image file as input, which is used as input into OpenFace's facial recognition algorithm specifically designed for images (FaceLandmarkImg.exe). Once the algorithm completes its analysis of the image, an output image and CSV file are generated containing the data generated from the algorithm. For example, the output image generated for the example photo in the repo looks like this:

![alt text](https://i.imgur.com/iFV1rWm.jpg "Isn't Gaben beautiful?")

Once these output files are generated, the script then uses Python's built-in CSV reading capabilities to read the locations of the generated facial action units to use as MIDI note inputs.

To convert this data into acceptable MIDI note inputs, the script makes use of the [pretty-MIDI Python Library](https://github.com/craffel/pretty-midi) (which will install itself automatically via PIP). As noted by the General MIDI Guidelines, MIDI note pitches are defined as a range of numbers spanning from 21 to 108. To remain compliant with this range, the script takes inputs taken from the generated CSV and continuously divides their value by 2 until their value lies within the acceptable MIDI pitch range.

![alt text](https://i.imgur.com/PmSQoq1.gif "General MIDI Pitch Guidelines as Used by pretty-MIDI")

An issue that comes with this method is the fear that all generated notes will sounds relatively similar to each other, therefore other methods of ensuring compliancy with the MIDI pitch range will be investigated.

Once the script generates MIDI notes for each facial action unit, an output MIDI is generated and located in the root directory of the project. For the example photo in the repo, the generated MIDI sounds like this:

[A Beautiful Output Face Melody](https://soundcloud.com/kaleb-byrum/piano-melody-generated-by-gabe-newells-face)

## This Music Isn't My Taste. What's the Point of This?
I created this project to test what musical capabilities could come from using OpenFace's facial recognition algorithm, and in turn, what musical applications could come from this computer vision innovation. I plan to push this project further by implementing real-time musical output using a webcam stream, which opens a door of opportunities, including using facial action units as inputs to multiple musical instruments, vis-a-vis, a face orchestra!

## Let's work together!
If you have interest in pushing this project further in a direction as mentioned above, feel free to fork and begin your own work! Feel free to contact me with ideas revolving around facial input musical applications, and together we can make something truly extraordinary.

Yours in Musicality,
Kaleb Byrum
kalebbyrum@aol.com
GitHub: kabyru
