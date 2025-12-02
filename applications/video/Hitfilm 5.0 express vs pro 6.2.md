---
date created: 2018-02-10
tags:
  - Video
modified: 2025-07-21
---
# Hitfilm 5.0 express vs pro 6.2

Hitfilm 5.0 express vs pro 6.2
zaterdag 10 februari 2018
7:34
De gele tekst zitten enkel in de Pro

## Audio

A range of audio effects are included to adjust your audio.
Audio Reverse
Plays the selected clip backwards.
Balance
Pan the audio from left to right within the stereo field of your project.
| •   | **Balance:** Negative values pan the audio farther to the left channel, and positive values pan it to the right channel. Zero sends the audio in equal amounts to both channels. |
|-----|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
Cathedral
Simulate the acoustics of a cathedral/large cavernous space.
| •   | **Gain:** Reduces or increases the overall volume of the processed audio signal. |
|-----|----------------------------------------------------------------------------------|
Channel Levels
Used to adjust the volume of each audio channel individually.
| •   | **Left:** Adjusts the overall level of the Left channel, in a dB scale. 0.0 dB is the original source volume. |
|-----|---------------------------------------------------------------------------------------------------------------|
| •   | **Right:** Adjusts the overall level of the Right channel, in a dB scale. 0.0 dB is the original source volume. |
|-----|-----------------------------------------------------------------------------------------------------------------|
Compressor
Compression reduces the total range in volume between the loudest and quietest points in the audio. This allows you to either reduce the audio peaks without making the quiet bits too quiet,or increase the level of the quiet moments without pushing the peaks too high, and causing them to clip.
| •   | **Input Gain:** Adjusts the gain of the source audio being fed into the Compressor effect. |
|-----|--------------------------------------------------------------------------------------------|
| •   | **Threshold:** The Threshold is the level above which the audio will be compressed, and below which the audio will remain unaffected. |
|-----|---------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Limiter:** Sets a fixed level which the audio peaks will not be allowed to exceed. Limiting should be used judiciously, because excessive clipping can cause unwanted distortion. |
|-----|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Ratio (x:1):** The ratio at which audio levels will be attenuated once they exceed the Threshold. |
|-----|-----------------------------------------------------------------------------------------------------|
| •   | **Knee:** Low values will result in a hard knee, or a severe transition at the threshold, while higher values will create a soft knee, and a more gentle transition from uncompressed to compressed audio. |
|-----|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Attack Time:** Defines how quickly, in milliseconds, the audio will be compressed once it exceeds the Threshold. Faster attack times are good for ensuring that extreme peaks in the audio are caught and reduced right away. |
|-----|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Release Time:** Defines how quickly, in milliseconds, the compressor will stop reducing the audio level, once the source level falls below the threshold. |
|-----|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Output Gain:** Sets the overall level of the audio after the compression has been applied. |
|-----|----------------------------------------------------------------------------------------------|
Doppler Shift
When combined with an animated layer, this effect introduces realistic Doppler Shift to an audio layer.
The effect should be added directly to your audio layer. In the effect's properties you can link it to a separate layer, which can then be animated. For example, if a point layer is created and animated to move towards camera, the audio will receive a Doppler Shift as if the sound is approaching camera.
A practical example would be to use a constant audio recording of a helicopter, which is then linked via the Doppler Shift effect to an animated 3D helicopter in your scene. The helicopter audio will be shifted automatically as the vehicle moves.
| •   | **Sound Position:** Use this menu to select any layer on your timeline. The selected layer's position will be used to calculate the Doppler Shift. |
|-----|----------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Speed of Sound:** Defined in meters per second. Works in conjunction with the **Scene Size**, which defines how many pixels are equal to a meter within your specific scene. |
|-----|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Scene Size:** Defines how many pixels in the scene correspond to a real meter. This makes it possible to get accurate Doppler Shifting for a variety of scene setups. |
|-----|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Distance Falloff:** When activated, the audio will diminish in volume the farther away it is from the position set in the **Volume Distance**. |
|-----|--------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Volume Distance** is the distance from the camera at which audio will be at 100% volume. As audio gets farther away it will become quieter. At the default of 1000px, if the audio moves closer to camera it will become louder than 100%. |
|-----|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
Echo
Generates echoes from the original audio. You can adjust the number of echoes, and how delayed they are from the original. The falloff determines how much of the echo is heard before it diminishes and becomes inaudible.
| •   | **Delay:** The time in milliseconds between the original audio signal, and the start of the echo. When the **Number of Echoes** is set higher than one, this value is also used to set the amount of time between the start of each echo. |
|-----|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Falloff:** Defines how much the Level of each echo will be reduced from the previous instance. At the default setting of 50%, the first echo will be half the level of the original signal, the second echo will be 25% of the original level, etc. |
|-----|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Number of Echoes:** The number of times the original audio will be repeated in echo. |
|-----|----------------------------------------------------------------------------------------|

Equalizer
The equalizer is used to adjust the strength of specific frequencies in an audio clip. This can be used to selectively adjust the bass and treble, for example, depending on the intent.
The presets menu provides quick access to common equalization tasks, such as high pass, low pass and bass boost.
The Master Gain control is used to control the volume of the clip. This operates separately to the volume property of the clip and should be used to set the base volume of an audio clip. The volume property can then be used to fine tune volume and mix clips over time.
Recorded audio will often have a low gain when imported. To set your gain to a satisfactory volume for standard playback on typical equipment, you can observe the default gain using the audio meters. Playback the clip and note the peak audio level, as displayed in the peak boxes. You can then make the appropriate adjustment to the Master Gain. For example, if you have a dialogue track which has been recorded with a peak of -18dB, making it rather quiet in the mix, you can set the Master Gain to 9.00dB in order to raise the overall gain to -9dB. This results in louder audio while still leaving headroom to adjust the volume if required.
Large Room
Simulates the ambient reverb of a large room. A longer reverb than the **Medium Room** effect.
| •   | **Gain:** Reduces or increases the overall volume of the processed audio signal. |
|-----|----------------------------------------------------------------------------------|
Medium Room
Simulates the ambient reverb of a medium sized room.
| •   | **Gain:** Reduces or increases the overall volume of the processed audio signal. |
|-----|----------------------------------------------------------------------------------|
Noise Reduction
This is a quick way to clean up audio which is suffering from unwanted background noise.
After applying the effect, move the playhead to a frame containing the noise you wish to remove, and no other audio. This should be a frame where there is no other interfering noises. For this reason when recording audio is is always worth recording a section of 'clean' audio before recording your actual subject. Clicking the **Capture Noise Print** button samples the audio contained in frame, so that HitFilm can recognize the noise.
| •   | **Capture Noise Print:** Clicking this button records whatever audio is present at the current playhead location. The effect will then use this Noise Print to remove the noise from all other frames of the video. |
|-----|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
Once you have Captured a Noise Print, some additional controls will appear. In many cases the noise will be immediately removed. The controls also allow you to fine tune how the noise removal is handled.
| •   | **Reset Noise Print:** Removes the noise print, so you can select a different frame. |
|-----|--------------------------------------------------------------------------------------|
| •   | **Add to Noise Print:** Allows you to select additional frames of noise, and add them to the noise print. |
|-----|-----------------------------------------------------------------------------------------------------------|
| •   | **Threshold Level:** On frames where the noise print overlaps with your dialog or other desired audio, removing all of the noise can sometimes create unnatural results. Reducing the Threshold Level restores a bit of the noise, can can be effective for getting a more natural result, while still retaining significant Noise Reduction. |
|-----|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Reduce By:** Defines, in dB, how much the noise print will be reduced in each frame of your video. If the results of the reduction are sounding unnatural, try lowering the Reduce By value, so the noise is not removed entirely. |
|-----|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
Pitch
Adjusting the pitch can be useful for particular effects, or to counter the natural pitch change caused by adjusting playback speed of a clip.
| •   | **Semitone Shift:** Sets, in semitones, how far the audio is shifted. Moving the slider to the left will shift the pitch lower, and moving to the right will shift the pitch higher. A semitone is equal to the pitch change between one key and the next on the piano. From C to C#, for example, is a semitone. 12 semitones is an octave. |
|-----|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
Shortwave Radio
Simulates the sound of a shortwave radio.
| •   | **Gain:** Reduces or increases the overall volume of the processed audio signal. |
|-----|----------------------------------------------------------------------------------|
Small Room
Simulates the ambient reverb of a small room. A shorter reverb than the **Medium Room** effect.
| •   | **Gain:** Reduces or increases the overall volume of the processed audio signal. |
|-----|----------------------------------------------------------------------------------|
Telephone
Simulates the sound of telephone audio.
| •   | **Gain:** Reduces or increases the overall volume of the processed audio signal. |
|-----|----------------------------------------------------------------------------------|
Tone
Generates a continuous tone of a defined frequency. The **Type** you select makes a bigger difference at lower Frequencies. The higher the **Frequency**, the harder it is to distinguish between the Types.
**Type**
| •   | **Sine:** A Sine wave gives a smooth, rounded sound. |
|-----|------------------------------------------------------|
| •   | **Square:** A Square wave gives a harsh, cutting sound |
|-----|--------------------------------------------------------|
| •   | **Frequency:** Sets the number of waves per second, which defines the pitch of the tone that is generated. |
|-----|------------------------------------------------------------------------------------------------------------|
**Behaviors**

Behaviors are a new variety of Effects introduced in HitFilm Pro in late 2017. They can be applied to layers to control the layer's movement using physics equations or values taken from another layer.
Behaviors can only be used on layers in composite shot timelines, and are not available in the Editor.
Acceleration \[Layer Only\]
Causes the layer to accelerate in a user-specified direction.
| •   | **Acceleration:** Sets the speed at which acceleration will occur. The distance the layer travels per second will be increase by the specified number of pixels for each second of travel. So if Acceleration is set to 100, for example, the layer will travel 100 pixels in the first second, 200 pixels in the second second, and 300 pixels in the third second, for a total of 600 pixels traveled in three seconds. |
|-----|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Orientation:** Sets the direction, in degrees in which travel will occur.The **X Axis**, **Y Axis**, and **Z Axis** are all represented, so you can move the layer in any direction you wish. |
|-----|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
Attract To \[Layer Only\]
This behavior allows you to move the layer it has been applied to toward the specific location of another layer. This is sometimes simpler that determining the exact angles in which a layer needs to move. For example, you can set up a Point layer at the exact destination you want to use, then select that point layer as a Target in the Attract To controls.
| •   | **Target:** The layer containing the Attract To behavior will move toward the position of the layer you select in this menu. |
|-----|------------------------------------------------------------------------------------------------------------------------------|
| •   | **Acceleration:** Sets the speed at which acceleration will occur. The distance the layer travels per second will be increase by the specified number of pixels for each second of travel. So if Acceleration is set to 100, for example, the layer will travel 100 pixels toward the Target in the first second, 200 pixels in the second second, and 300 pixels in the third second, for a total of 600 pixels traveled in three seconds. |
|-----|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Distance:** |
|-----|---------------|
| •   | **Falloff:** Choose between Linear and Quadratic Falloff |
|-----|----------------------------------------------------------|
| •   | **Target Radius:** |
|-----|--------------------|
Drag \[Layer Only\]
When drag is applied to a layer, any movement of the layer will be slowed down based on the amount of drag applied. The higher the Drag value, the slower the layer will move, and the less distance it will cover.
| •   | **Drag:** Specifies the amount of drag applied to the layer's motion. |
|-----|-----------------------------------------------------------------------|
Follow \[Layer Only\]
The Follow behavior allows you to move the layer it has been applied to based on the movement of another layer.
| •   | **Target:** The layer containing the Follow effect will follow the movement of the layer you select in this menu. |
|-----|-------------------------------------------------------------------------------------------------------------------|
| •   | **Attraction:** Defines the strength of the attraction between the two layers. |
|-----|--------------------------------------------------------------------------------|
| •   | **Distance:** Sets the closest distance the two layers will get to one another. Once the layer the Follow effects is applied to reaches this distance from the Target layer, it will stop. |
|-----|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
Gravity \[Layer Only\]
The Gravity behavior drags your layer downward at a progressively accelerating rate, like actual gravity.
| •   | **Acceleration:** Sets the speed at which acceleration will occur. The distance the layer travels per second will be increase by the specified number of pixels for each second of travel. So if Acceleration is set to 100, for example, the layer will travel 100 pixels toward the Target in the first second, 200 pixels in the second second, and 300 pixels in the third second, for a total of 600 pixels traveled in three seconds. |
|-----|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
Mix Parent Position \[Layer Only\]
This behavior allows you to adjust the intensity of the parenting between layers. While standard parenting is absolute, and always affects the child layer at 100% of the parent layer's position values, you can use Mix Parent Position to reduce the impact that parenting has on the child.
| •   | **Source Layer:** This menu is used to select the Layer whose position you wish to use as a source. |
|-----|-----------------------------------------------------------------------------------------------------|
| •   | **Mix:** Sets the percentage of the source layer's movement that will be applied to this layer. If the Mix is set to 70%, for example, and the Source layer moves 100 pixels down and 200 pixels to the left, the layer the Mix Parent Position behavior is applied to will move 70 pixels down and 140 pixels to the left. |
|-----|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
Repel From \[Layer Only\]
This behavior moves the layer it has been applied to away from the specific location of another layer. This allows you to push one layer around using a second layer, and keep a minimum distance between them.
| •   | **Target:** The layer containing the Repel From behavior will move away from the position of the layer you select in this menu. |
|-----|---------------------------------------------------------------------------------------------------------------------------------|
| •   | **Acceleration:** Sets the speed at which repulsion will be accelerated. The distance the layer travels per second will be increase by the specified number of pixels for each second of travel. So if Acceleration is set to 100, for example, the layer will travel 100 pixels toward the Target in the first second, 200 pixels in the second second, and 300 pixels in the third second, for a total of 600 pixels traveled in three seconds. |
|-----|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Distance:** The minimum separation between this layer and the Target Layer. Once the tow layers reach this distance from one another, this layer will begin moving away from the target layer. |
|-----|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Falloff:** Choose between Linear and Quadratic Falloff |
|-----|----------------------------------------------------------|
Rotate By Layer \[Layer Only\]
This behavior allows you to adjust the intensity of the parenting between layers. While standard parenting is absolute, and always affects the child layer at 100% of the parent layer's rotation values, you can use Mix Parent Position to reduce the impact that parenting has on the child. Each axis is separated, so they can be controlled independently
| •   | **Rotate By Layer:** This menu is used to select the Layer whose rotation values you wish to use as a source. |
|-----|---------------------------------------------------------------------------------------------------------------|
| •   | **Rotation X Amount:** Sets the percentage of the source layer's X rotation that will be applied to this layer. If the Mix is set to 50%, for example, and the Source layer rotates 180 degrees on the X axis, the layer the Mix Parent Position behavior is applied to will rotate 90 degrees on the X axis. |
|-----|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Rotation Y Amount:** Sets the percentage of the source layer's Y rotation that will be applied to this layer. If the Mix is set to 50%, for example, and the Source layer rotates 180 degrees on the Y axis, the layer the Mix Parent Position behavior is applied to will rotate 90 degrees on the Y axis. |
|-----|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Rotation Z Amount:** Sets the percentage of the source layer's Z rotation that will be applied to this layer. If the Mix is set to 50%, for example, and the Source layer rotates 180 degrees on the Z axis, the layer the Mix Parent Position behavior is applied to will rotate 90 degrees on the Z axis. |
|-----|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
Throw \[Layer Only\]
Causes the layer to travel in a user-specified direction. The Throw behavior is similar to the Accelerate behavior, except the object travels at a consistent speed
| •   | **Speed:** Sets the speed at which movement will occur, in pixels per second. |
|-----|-------------------------------------------------------------------------------|
| •   | **Accelerate Time:** The amount of time, in seconds, which the layer will take to accelerate from a stationary position to full speed. After the Accelerate time, the layer will continue to move at a fixed rate of Speed, in the direction you have chosen. |
|-----|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Orientation:** Sets the direction, in degrees in which travel will occur.The **X Axis**, **Y Axis**, and **Z Axis** are all represented, so you can move the layer in any direction you wish. |
|-----|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

**Blurs**

The Blurs folder contains all of the blur-related effects.
Some blurs include a **Clamp to Edge** property, which ensures that the effect extends to the edge of the frame.
See [Motion Blur](http://hitfilm.com/reference/hitfilm-pro/motion_blur.htm#hmpopupDiv) for information on the automatic motion blur feature.
Angle Blur
Blurs the layer in a specific direction. Can be useful for an impression of fast movement.
![image1](image1-53.png)
| •   | **Angle:** Rotating the Angle wheel controls the direction of the blur |
|-----|------------------------------------------------------------------------|
| •   | **Length:** Sets the strength of the blur, defined in number of pixels |
|-----|------------------------------------------------------------------------|
| •   | **Clamp To Edge:** Enabling this feature prevents the blur from expanding outside the edges of the layer it is applied to. Disabling it will allow the blur to expand outside the layer edges. |
|-----|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
Bilateral Blur
Smooths images for a softer, untextured appearance, while retaining fine edge detail.
![image2](image2-25.png)
| •   | **Radius:** Sets the intensity of the blur.The radius, in pixels, defines the area that will be calculated into the blur of each pixel. |
|-----|-----------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Threshold:** Sets the amount of edge contrast that must be present for an edge to be retained. Higher values will result in fewer edges being held out from the blur. |
|-----|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Dimension:** The blur can be applied **Horizontally, Vertically,** or **Both**. |
|-----|-----------------------------------------------------------------------------------|
Blur
A standard, fast blur.
![image3](image3-13.png)
| •   | **Radius:** Sets the intensity of the blur.The radius, in pixels, defines the area that will be calculated into the blur of each pixel. |
|-----|-----------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Iterations:** The number of times the blur is calculated. More iterations give a smoother result, and a larger blur. |
|-----|------------------------------------------------------------------------------------------------------------------------|
| •   | **Dimension:** The blur can be applied **Horizontally, Vertically,** or **Both**. |
|-----|-----------------------------------------------------------------------------------|
| •   | **Clamp To Edge:** Enabling this feature prevents the blur from expanding outside the edges of the layer it is applied to. Disabling it will allow the blur to expand outside the layer edges. |
|-----|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
Diffuse
Creates a soft focus appearance by duplicating the footage, blurring the copy, and then blending the duplicate back onto the original footage.
![image4](image4-12.png)
| •   | **Radius:** Sets the intensity of the blur.The radius, in pixels, defines the area that will be calculated into the blur of each pixel. |
|-----|-----------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Opacity:** Controls the opacity of the duplicate blurred footage. Lower opacity levels will give a more subtle result. |
|-----|---------------------------------------------------------------------------------------------------------------------------|

Lens Blur
The lens blur is designed to more closely mimic the depth of field bokeh effects created by real lenses. It can be used in conjunction with a depth map to selectively blur different areas of the frame to different degrees.
Here's an example of lens blur in action:
![image5](image5-9.png)
Here is the original frame:
![image6](image6-8.png)
Note how the face remains in sharp focus while the rest of the image becomes progressively more blurred. This is based upon a simple depth map created by hand inside HitFilm using some planes and masks:
![image7](image7-4.png)
The circle at the top keeps the face in focus, while the left-to-right gradient oval causes her arm to become progressively more blurred. The rest of the image, being black, is fully blurred.
Lens blur can be heavily customized.
| •   | **Source Layer:** can be optionally used to apply a depth map, as shown in the example above. |
|-----|-----------------------------------------------------------------------------------------------|
| •   | **Source Channel:** You can use various **channels** from the source layer as the depth map, such as luminance and alpha. |
|-----|---------------------------------------------------------------------------------------------------------------------------|
| •   | **Radius:** adjusts the strength of the blur. |
|-----|-----------------------------------------------|
| •   | **Focal Distance:** is used to rack focus based on the depth map, adjusting which point on the map is in focus. This is analogous to changing focus on your camera. |
|-----|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Focal Range:** defines the depth of field. A larger focal range will cause more of the frame to remain in focus, while a small focal range will cause a shallower area to remain in focus. |
|-----|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Specular Threshold:** Sets the luminance level above which highlights will be blown out to white, rendering as specular highlights based on the Iris settings below. |
|-----|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Specular Brightness:** sets the brightness of the specular highlights. Lower threshold and higher brightness will make the bokeh more obvious. The bokeh shape can be further customized in the **Iris** section. |
|-----|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Quality:** defines the visual quality of the blur. If you are trying to match your footage to other footage shot with a lower quality lens, reducing the quality may help. Reducing quality also allows the effect to render more quickly. |
|-----|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
**Iris**
The iris section can be used to switch between multiple primitive shapes. These can then be rotated and warped using the **curvature**, **pinch** and **shift** options to create custom shapes. The **View Iris** option can be useful for dialing in the shape of the iris.
| •   | **Shape:** Select a shape based on the number of blades you wish to be used for the iris. More blades tend to give a smoother blur and higher quality results. |
|-----|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Rotation:** Sets the rotation of the shape selected above. |
|-----|--------------------------------------------------------------|
| •   | **Curvature:** Sets the curvature of each blade of the iris. A value of 0.0 creates a straight side. Negative values will curve the sides inward, while positive values curve it outward. |
|-----|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Pinch:** Limits the area affected by the curvature. Higher pinch levels will reduce the width of the curve, so it is pinched close to the vertices of the iris shape. |
|-----|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Shift:** Offsets the center of the curvature. |
|-----|-------------------------------------------------|
| •   | **Opacity Curve:** Feathers the edges of the iris shape, from the outer edge and the center. |
|-----|----------------------------------------------------------------------------------------------|
| •   | **Highlight Location:** Sets the distance of the circular highlight from the center of the iris. |
|-----|--------------------------------------------------------------------------------------------------|
| •   | **View Iris:** Enabling this option shows the iris shape in white, so you can see exactly how the adjustments above affect the shape that will be used to render the specular highlights. |
|-----|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
Motion Blur
This uses optical flow techniques to identify movement in a layer and apply artificial motion blur. This can be very useful for animation or for adding exaggerated motion blur to a live action shot.
![image8](image8-3.png)
| •   | **Mode:** You can use the default settings used by the entire composite shot by selecting **Comp Settings**, or use **Custom** settings. If you select Custom, the following settings will become available. |
|-----|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
**Custom**
| •   | **Shutter Angle:** A larger shutter angle will create more motion blur. The shutter angle simulates the amount of time a real camera shutter is open. |
|-----|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Shutter Phase:** Positions the blur in relation to the moving object. This can be used to offset the blur in front or behind the object. For realistic motion blur this is best kept to half the value of the shutter angle. |
|-----|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Samples:** Motion blur is constructed by sampling the position of the layer over multiple frames. A higher number of samples will result in a higher quality motion blur. Fewer samples will be faster to render but may introduce visible banding in the motion blur. |
|-----|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
**Optical Flow**
Motion blur is calculated by tracking the movement of every pixel in the image using optical flow techniques. The amount of blur applied to each pixel is based on the speed at which it is moving. These advanced settings let you adjust how the movement in the frame is tracked.
| •   | **Window Size:** The number of pixels surrounding the current pixel that is scanned to calculate the motion of the current pixel. |
|-----|-----------------------------------------------------------------------------------------------------------------------------------|
| •   | **Sigma:** A value in the algorithm used for tracking, that alters the way it tracks. Changing the Sigma can affect the result. If the blur is calculated incorrectly, trial and error can be used to see if changing sigma improves results. |
|-----|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Iterations:** The number of times the tracking algorithm is performed. The results of all iterations are averaged, so more iterations will give a more accurate result, but will also take longer to calculate. |
|-----|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Downsamples:** Optical Flow can only track movement smaller than one pixel, so before the tracking algorithm runs, the image must be downsampled. You can create multiple levels of downsampling, and the algorithm will be calculated for each downsample level. More downsamples can improve the results, but will take longer to calculate. |
|-----|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Start Downsample:** By default the tracking algorithm starts with the first downsample, skipping the full resolution image, which makes it less susceptible to being misled by noise in the image. Increasing the Start Downsample can speed up the results, but reduces the resolution of the tracking results, which may negatively impact accuracy. |
|-----|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
Radial Blur
Creates a circular shaped blur. The center of the blur can also be moved using the control point in the Viewer.
![image9](image9-3.png)
| •   | **Center Position:** The center point from which the blur is calculated can be positioned anywhere you like. You can either manually type in a value, or select the Position property, then drag the Center Point shown in the Viewer to a new location. |
|-----|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Use Layer:** If you wish to link the center of the blur to the position of a different layer, you can use this property to select any layer on your timeline. |
|-----|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Angle:** Controls the amount of blur applied. Since radial blur has a greater effect on the image the farther you get from the center point, the amount of blur is defined in degrees, rather than pixels. |
|-----|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
Zoom Blur
A blur emanating out from a central point. The center of the blur can also be moved using the control point in the Viewer.
![image10](image10-3.png)
| •   | **Quality:** Affects the smoothness of the blurred results. Increasing the quality will smooth the results, but may take longer to calculate. |
|-----|-----------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Strength:** The distance, in pixels, that each pixel will be blurred. |
|-----|-------------------------------------------------------------------------|
| •   | **Center Position:** The center point from which the blur is calculated can be positioned anywhere you like. You can either manually type in a value, or select the Position property, then drag the Center Point shown in the Viewer to a new location. |
|-----|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Use Layer:** If you wish to link the center of the blur to the position of a different layer, you can use this property to select any layer on your timeline. |
|-----|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|

**Channel**
Channel effects are used to manipulate the channels in a layer, such as RGB or luminance.
Channel Blur
Blurs channels individually. Useful for creating the impression of chromatic aberration.
![image11](image11-2.png)

![image12](image12-2.png)
**Radius**
| •   | **Radius Red:** Sets the radius of the blur on the red channel. A higher radius creates a bigger blur. |
|-----|--------------------------------------------------------------------------------------------------------|
| •   | **Radius Green:** Sets the radius of the blur on the green channel. A higher radius creates a bigger blur. |
|-----|------------------------------------------------------------------------------------------------------------|
| •   | **Radius Blue:** Sets the radius of the blur on the blue channel. A higher radius creates a bigger blur. |
|-----|----------------------------------------------------------------------------------------------------------|
| •   | **Radius Alpha:** Sets the radius of the blur on the alpha channel, which determines the transparency of the image. A higher radius creates a bigger blur. |
|-----|------------------------------------------------------------------------------------------------------------------------------------------------------------|
**Dimension**
| •   | **Dimension Red:** Select whether the red channel blur is **Horizontal**, **Vertical**, or both **Horizontal and Vertical**. |
|-----|------------------------------------------------------------------------------------------------------------------------------|
| •   | **Dimension Green:** Select whether the green channel blur is **Horizontal**, **Vertical**, or both **Horizontal and Vertical**. |
|-----|----------------------------------------------------------------------------------------------------------------------------------|
| •   | **Dimension Blue:** Select whether the blue channel blur is **Horizontal**, **Vertical**, or both **Horizontal and Vertical**. |
|-----|--------------------------------------------------------------------------------------------------------------------------------|
| •   | **Dimension Alpha:** Select whether the alpha channel blur is **Horizontal**, **Vertical**, or both **Horizontal and Vertical**. |
|-----|----------------------------------------------------------------------------------------------------------------------------------|
Channel Mixer
Used to mix the color channels together. The red channel can have some of the blue channel introduced to it, for example. This can be useful for adjusting the color balance in a natural way, since the adjustments are based on another color channel from the source image.
![image11](image11-2.png)

![image13](image13-2.png)
The channel mixer is an effective option for creating a black and white image with extensive control over the contrast. Setting all values to zero, and then increasing the Red value in each color channel to 1.0, for example, will give you a black & white image of only the red channel. The same technique can be used with the green or blue channels as well.
**Red**
| •   | **Red:** Sets the amount of the source red channel that is used to create the red output of your image. The default value of 1.0 delivers the red channel in its original state. |
|-----|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Green:** Sets the amount of the source green channel that is used to create the red output. This is set to 0.0 by default. Decreasing this value will darken the red output, based on the contrast contained in the green channel. Increasing the value will brighten the red output, based on the contrast of the green channel. |
|-----|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Blue:** Sets the amount of the source blue channel that is used to create the red output. This is set to 0.0 by default. Decreasing this value will darken the red output, based on the contrast contained in the blue channel. Increasing the value will brighten the red output, based on the contrast of the blue channel. |
|-----|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Const:** Controls the base value of the red channel. This value is calculated after the three channels above are mixed, and increases or decreases the total output of the red channel, based on the sum of the three channels above. |
|-----|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
**Green**
| •   | **Red:** Sets the amount of the source red channel that is used to create the green output of your image. This is set to 0.0 by default. Decreasing this value will darken the green output, based on the contrast contained in the red channel. Increasing the value will brighten the green output, based on the contrast of the red channel. |
|-----|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Green:** Sets the amount of the source green channel that is used to create the green output of your image. The default value of 1.0 delivers the green channel in its original state. |
|-----|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Blue:** Sets the amount of the source blue channel that is used to create the green output. This is set to 0.0 by default. Decreasing this value will darken the green output, based on the contrast contained in the blue channel. Increasing the value will brighten the green output, based on the contrast of the blue channel. |
|-----|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Const:** Controls the base value of the green channel. This value is calculated after the three channels above are mixed, and increases or decreases the total output of the red channel, based on the sum of the three channels above. |
|-----|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
**Blue**
| •   | **Red:** Sets the amount of the source red channel that is used to create the blue output of your image. This is set to 0.0 by default. Decreasing this value will darken the blue output, based on the contrast contained in the red channel. Increasing the value will brighten the blue output, based on the contrast of the red channel. |
|-----|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Green:** Sets the amount of the source green channel that is used to create the blue output. This is set to 0.0 by default. Decreasing this value will darken the blue output, based on the contrast contained in the green channel. Increasing the value will brighten the blue output, based on the contrast of the green channel. |
|-----|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Blue:** Sets the amount of the source blue channel that is used to create the blue output of your image. The default value of 1.0 delivers the blue channel in its original state. |
|-----|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Const:** Controls the base value of the blue channel. This value is calculated after the three channels above are mixed, and increases or decreases the total output of the blue channel, based on the sum of the three channels above. |
|-----|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
Channel Swapper
Replaces channels with other channels. For example, you can have a layer's alpha (transparency) set to correspond to its red values, or its saturation. This is useful for both color grading and compositing. Channel swapping is also frequently used in Infrared (IR) photography.
![image11](image11-2.png)

![image14](image14-2.png)
| •   | **Take Red From:** Select the source channel that will be used to generate the red output. |
|-----|--------------------------------------------------------------------------------------------|
| •   | **Take Green From:** Select the source channel that will be used to generate the green output. |
|-----|------------------------------------------------------------------------------------------------|
| •   | **Take Blue From:** Select the source channel that will be used to generate the blue output. |
|-----|----------------------------------------------------------------------------------------------|
| •   | **Take Alpha From:** Select the source channel that will be used to generate the alpha output. |
|-----|------------------------------------------------------------------------------------------------|
Channel Time Shift
Moves red, green and blue channels backwards or forwards in time individually. This creates a trailing effect on moving objects, or can create a chromatic aberration style distortion.
![image15](image15-2.png)
| •   | **Red Shift:** Sets the number of frames by which the red channel is shifted from the current frame number. Positive values will take frames from later in the clip, while negative values will take frames from earlier in the clip. |
|-----|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Green Shift:** Sets the number of frames by which the green channel is shifted from the current frame number. Positive values will take frames from later in the clip, while negative values will take frames from earlier in the clip. |
|-----|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Blue Shift:** Sets the number of frames by which the blue channel is shifted from the current frame number. Positive values will take frames from later in the clip, while negative values will take frames from earlier in the clip. |
|-----|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Alpha:** Selects the frame that will be used for the alpha channel. By default it uses the **Current Frame**. **Average** will calculate the average of the values of all three color channels, and use that frame. **Red Shift**, **Green Shift** and **Blue Shift** will take the value from the selected channel, and use that frame as the alpha. The alpha setting applies when you are working with a layer that included alpha transparency. On standard video, the alpha setting will have no effect, since the entire frame is completely opaque. |
|-----|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
Color Space Converter
Changes the color space of the layer to a different color space. Useful for color grading and compositing.
![image11](image11-2.png)

![image16](image16-1.png)
| •   | **From:** Select the source channel or color space from which the conversion will be calculated. |
|-----|--------------------------------------------------------------------------------------------------|
| •   | **To:** Select the destination color space to which the source channel or color space will be converted. |
|-----|----------------------------------------------------------------------------------------------------------|
| •   | **Invert:** Toggling this option will invert the results of the conversion. |
|-----|-----------------------------------------------------------------------------|
| •   | **Alpha:** Controls how the alpha channel is handled. **Normal** will give the typical result based on the conversion options you have selected. **Solid** will override the conversion settings and create a solid alpha, so the layer remains entirely opaque. |
|-----|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

**Color Correction**

Color correction effects are designed to enhance the visual quality of layers by adjusting their colors. Color correction is intended for the initial color manipulation and for fixing problems.
Also see [Color Grading](http://hitfilm.com/reference/hitfilm-pro/color_2.htm#hmpopupDiv).
Auto Color
HitFilm includes three Auto grading effects to adjust the layer's color, contrast or levels.
Compare the following image in each of these three effects to see the different results they give.
![image17](image17-1.png)

![image18](image18-1.png)
| •   | **Threshold:** sets the threshold below which colors will remain unaffected. |
|-----|------------------------------------------------------------------------------|
| •   | **Blend With Original:** the effect of the Auto Color can be softened by increasing this setting. Higher values retain more of the original color. |
|-----|----------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Select Frame:** by default the auto grading effects update on each frame, which can cause fluctuations in the layer's appearance as the contents of the frame change. By activating the **Select frame** property you can manually choose a frame to use as the source for the automatic adjustment, which will be used for the duration of the layer. |
|-----|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
Auto Contrast
HitFilm includes three Auto grading effects to adjust the layer's color, contrast or levels.
Compare the following image in each of these three effects to see the different results they give.
![image17](image17-1.png)

![image19](image19-1.png)
| •   | **Threshold:** sets the threshold below which colors will remain unaffected. |
|-----|------------------------------------------------------------------------------|
| •   | **Blend With Original:** the effect of the Auto Contrast can be softened by increasing this setting. Higher values retain more of the original color. |
|-----|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Select Frame:** by default the auto grading effects update on each frame, which can cause fluctuations in the layer's appearance as the contents of the frame change. By activating the **Select frame** property you can manually choose a frame to use as the source for the automatic adjustment, which will be used for the duration of the layer. |
|-----|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
Auto Levels
HitFilm includes three Auto grading effects to adjust the layer's color, contrast or levels.
Compare the following image in each of these three effects to see the different results they give.
![image17](image17-1.png)

![image20](image20-1.png)
| •   | **Threshold:** sets the threshold below which colors will remain unaffected. |
|-----|------------------------------------------------------------------------------|
| •   | **Blend With Original:** the effect of the Auto Levels can be softened by increasing this setting. Higher values retain more of the original color. |
|-----|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Select Frame:** by default the auto grading effects update on each frame, which can cause fluctuations in the layer's appearance as the contents of the frame change. By activating the **Select frame** property you can manually choose a frame to use as the source for the automatic adjustment, which will be used for the duration of the layer. |
|-----|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
Brightness & Contrast
Quick adjustment of the layer's brightness and contrast.
| •   | **Brightness:** adjust to the left to decrease brightness, or to the right to increase brightness. |
|-----|----------------------------------------------------------------------------------------------------|
| •   | **Contrast:** adjust to the left to decrease contrast, or to the right to increase contrast. |
|-----|----------------------------------------------------------------------------------------------|
Color Balance
Individually adjust the balance of red, green and blue in the layer's shadows, midtones and highlights.
![image11](image11-2.png)

![image21](image21-1.png)
The **Preserve luminosity** property retains the layer's original brightness when altering the colors.
**Shadows**
| •   | **Red Balance:** adjust to the left to reduce red tones in the shadow areas, or to the right to increase red tones in the shadow areas. |
|-----|-----------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Green Balance:** adjust to the left to reduce green tones in the shadow areas, or to the right to increase green tones in the shadow areas. |
|-----|-----------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Blue Balance:** adjust to the left to reduce blue tones in the shadow areas, or to the right to increase blue tones in the shadow areas. |
|-----|--------------------------------------------------------------------------------------------------------------------------------------------|
**Midtones**
| •   | **Red Balance:** adjust to the left to reduce red tones in the midtones, or to the right to increase red tones in the midtones. |
|-----|---------------------------------------------------------------------------------------------------------------------------------|
| •   | **Green Balance:** adjust to the left to reduce green tones in the midtones, or to the right to increase green tones in the midtones. |
|-----|---------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Blue Balance:** adjust to the left to reduce blue tones in the midtones, or to the right to increase blue tones in the midtones. |
|-----|------------------------------------------------------------------------------------------------------------------------------------|
**Highlights**
| •   | **Red Balance:** adjust to the left to reduce red tones in the highlights, or to the right to increase red tones in the highlights. |
|-----|-------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Green Balance:** adjust to the left to reduce green tones in the highlights, or to the right to increase green tones in the highlights. |
|-----|-------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Blue Balance:** adjust to the left to reduce blue tones in the highlights, or to the right to increase blue tones in the highlights. |
|-----|----------------------------------------------------------------------------------------------------------------------------------------|
Color Correction Wheels
This effect provides a visual way to quickly adjust the highlights, midtones and shadows of your layer.
You can drag on the color wheels to adjust the color balance of highlights (top wheel), midtones (middle wheel) and shadows (bottom wheel). The further out from the center of the color wheel you drag the point, the more saturated the colors will become.
The sliders can be used to adjust the strength and lightness of the adjustment, and the rotator on the wheels changes the hue.
Additional controls can be found in the property groups below the wheels, including a white balance property which functions the same as the separate **white balance** effect.
Here you can see the difference the color wheels effect can make to a layer, with the original shown first and the color corrected version below it:
![image22](image22-1.png)
Color Temperature
Use to warm or cool the colors in your layer. Color temperature is measured in Kelvin.
| •   | **Temperature:** adjusting to the left reduces color temperature, introducing more orange and red into the image. Adjusting to the right increases the color temperature, shifting it towards blue. |
|-----|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
Crush Blacks & Whites
An alternative to simply altering the contrast, this enables you to change the black and white points separately for finer control.
| •   | **Black:** Increasing this slider will raise the threshold below which shadow areas will be pushed into black |
|-----|---------------------------------------------------------------------------------------------------------------|
| •   | **White:** decreasing this slider lowers the threshold above which highlights will be pushed into White. |
|-----|----------------------------------------------------------------------------------------------------------|
Curves
Curves is a powerful color correction and grading tool, based on an editable graph. Here's an example of the curves graph as shown in the Controls panel:
![image23](image23.png)
The horizontal axis on the graph represents the input, which is the original image. The vertical axis represents the output, which is the graded result. Therefore if you follow a line vertically up from any point on the graph until you hit the curves, then track to the left, you can see how the input is being changed.
Therefore with the default curves graph you can see that the input values are identical to the output values:
![image24](image24-1.png)
Two easy presets are provided, one of which resets the graph to the default straight line and another which creates an s-curve:
![image25](image25-1.png)
Where the graph becomes steeper you will see increased contrast, whereas a shallower incline will reduce contrast. In the case of an s-curve, the center of the graph is steeper, which increases contrast in the mid-tones, at the expense of detail in the shadows and highlights.
Given that the focus of a frame is often in the mid-tones (such as actor's faces), an s-curve is often an effective way to add perceived detail and contrast to a shot.
Curves can be used to adjust the RGB channels combined or each channel individually. Adjusting individual channels can be useful for correcting white balance and lighting issues.
Custom Gray
This creates a grayscale image while providing finer control over how that image is generated. This is useful for creating specific black and white looks, as each RGB channel can be emphasized to a lesser or greater degree when creating the result, providing fine control over contrast.
![image26](image26-1.png)
| •   | **Red:** Positive values increase the lightness of the red channel, negative values decrease the lightness of the red channel. Increasing the red level can help lighten skin tones, to bring the viewer's focus onto human subjects. |
|-----|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Green:** Positive values increase the lightness of the green channel, negative values decrease the lightness of the green channel. |
|-----|--------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Blue:** Positive values increase the lightness of the blue channel, negative values decrease the lightness of the blue channel. |
|-----|-----------------------------------------------------------------------------------------------------------------------------------|
The sum of the values of the Red, Green, and Blue channels should equal 1.00 to maintain the overall luminosity of the original image. Total values above 1.00 will brighten the image overall, and total values below 1.00 will darken it.
| •   | **Offset:** Raises or lowers the luminosity of the entire image equally, affecting all tones in the image equally |
|-----|-------------------------------------------------------------------------------------------------------------------|
| •   | **Exposure:** Raises or lowers the exposure of the image. This adjustment primarily affects the Highlights and Midtones, while the Shadow areas remain unaffected. Thus, reducing Exposure lowers the overall contrast of the image, while increasing Exposure increases the contrast between the brightest and darkest areas. |
|-----|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
Exposure
Simulates the effect of letting more light into the camera lens. The end result is a brightening or darkening of the footage, but in a more natural, dynamic way than a direct Brightness adjustment. In addition to changing brightness, reducing Exposure lowers the overall contrast of the image, while increasing Exposure increases the contrast between the brightest and darkest areas. The available controls give you access to the three main tonal ranges of the image, allowing you to fine-tune the Highlights, Midtones, and Shadows separately.
![image11](image11-2.png)

![image27](image27-1.png)
| •   | **Exposure:** Primarily brightens or darkens the highlights of the image, with minimal effects on the shadows. |
|-----|----------------------------------------------------------------------------------------------------------------|
| •   | **Offset:** Brightens or darkens the shadow areas of the image, with minimal effects on the Highlights. Start with minor adjustments, as excessive changes here can create unnatural results. |
|-----|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Gamma:** Shifts the midtones of the image. |
|-----|----------------------------------------------|
Gamma
Individually alter the gamma of red, green and blue channels. Gamma is weighted toward the midtones of the image, and will change the midtones the most, with a more minimal impact on the highlights and shadows.
![image11](image11-2.png)

![image28](image28-1.png)
| •   | **Red:** Raises or lowers the red levels in the image, especially in the midtones. |
|-----|------------------------------------------------------------------------------------|
| •   | **Green:** Raises or lowers the green levels in the image, especially in the midtones. |
|-----|----------------------------------------------------------------------------------------|
| •   | **Blue:** Raises or lowers the blue levels in the image, especially in the midtones. |
|-----|--------------------------------------------------------------------------------------|
Hotspots
A quick and easy way to isolate and alter the bright areas of your layer. Hotspots allow you to select and modify the brightest areas of your image, based on a user-defined brightness threshold.
![image11](image11-2.png)

![image29](image29-1.png)
| •   | **Threshold:** Sets the brightness threshold on which the effect is based. Only areas above your Threshold setting will retain detail. |
|-----|----------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Threshold Add Color:** All areas of the image below the threshold level will be filled with the color you select here. By default the color is black, which can be useful for isolating the hot spots in your image for compositing purposes. For example, you could duplicate your footage, apply Hot Spots to the top copy, then set the blend mode of the top copy to Screen to blend the results of the Hot Spots effect onto the original copy of the footage below it. |
|-----|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Saturation:** Adjusts the intensity of the colors in any areas brighter than the Threshold. |
|-----|-----------------------------------------------------------------------------------------------|
| •   | **Brightness:** Alters the brightness of all areas in your footage which are brighter than the Threshold. |
|-----|-----------------------------------------------------------------------------------------------------------|
| •   | **Smooth Source:** Applies a blur to the source image before calculating the threshold, which is useful for smoothing the transition areas around the threshold and removing graininess in the result. |
|-----|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
Hue, Saturation & Lightness
Control over the hue, saturation and lightness of your image. The **Master** controls affect the entire image, while the individual color controls (**Red, Yellow, Green, Cyan, Blue, Magenta**) allow you to limit adjustments to a specific color family.
![image11](image11-2.png)

![image30](image30-1.png)
| •   | **Hue Shift:** Shifts the colors by rotating them the specified number of degrees around the color wheel. The colors are oriented around the color wheel in the sequence they are listed in the effect (red, yellow, green, cyan, blue, magenta), and the distance between each color family is 60 degrees. The Master control will affect the entire image, while the lower controls will only affect a range of colors within the specific color family you adjust. |
|-----|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Saturation:** Increases or decreases the saturation, or color intensity. The Master control will affect the entire image, or you can select a specific color family and adjust it separately from all other colors in the image. |
|-----|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Lightness:** Lightens or darkens the image. The Master control will affect the entire image, or you can select a specific color family and adjust it separately from all other colors in the image. Increasing the Lightness can result in a perceived decrease in saturation, so in many cases it may be useful to adjust Lightness and Saturation in combination to get the result you desire. |
|-----|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
The Master controls in the Hue, Saturation & Lightness effect are a quick way to adjust the overall Saturation and Lightness of your image.
Levels Histogram
Levels gives you detailed information about the channel composition of the layer through the use of a Histogram Display.This allows you to make manual adjustments to the tonality of the layer to improve its appearance. A Histogram is a graph which allows you to quickly see at a glance the exact range of tonal values in your image. Histograms are also available in the scopes panel, and more information about histograms is available in [Introducing Scopes](http://hitfilm.com/reference/hitfilm-pro/introducing_scopes.htm#hmpopupDiv). The histogram is a more accurate way to assess colors than by eye.
The histogram displays a readout of the tones in your image. The tones range from pure black on the left to pure white on the right. The height of the graph at any point indicates the relative frequency of that specific tone in the image. Information for different channels of your image can be viewed, based on your selection in the **Channels** menu.
**Channels Menu**
| •   | **RBG:** Displays three separate histograms at once, one for each color channel of your image. Each histogram is colored to match the channel it represents. |
|-----|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **RGB Combined:** Averages the values of all three channels, and displays a single histogram that represents the overall tonal values of the image. |
|-----|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Red:** Displays the tonal values of the Red channel of the image. |
|-----|---------------------------------------------------------------------|
| •   | **Green:** Displays the tonal values of the Green channel of the image. |
|-----|-------------------------------------------------------------------------|
| •   | **Blue:** Displays the tonal values of the Blue channel of the image. |
|-----|-----------------------------------------------------------------------|
| •   | **Alpha:** Displays the tonal values of the Alpha channel of the image. |
|-----|-------------------------------------------------------------------------|
**The Histogram**
The primary method for viewing the levels in your image is the Histogram. The image below is represented by the histogram shown to its right.
![image11](image11-2.png)

![image31](image31.png)
The histogram contains a **Graph** and a **Gradient**. Beneath the graph are three triangles, representing the **Input Black** (black triangle), the **Gamma** (grey triangle) and the **Input White** (white triangle). Looking at this histogram, notice that the graph does not begin at the Input Black, it ends before the Input White, and nearly all the image data is positioned below the mid-point Gamma control. By default, pure black is set to 0.0, and pure white is set to 1.0. Shifting the white or black input values evenly redistributes the tonal range of the image between black and white. However, adjusting them too far can result in clipping of the image, and loss of detail in the shadow or highlight areas.
By adjusting these controls we can optimize the dynamic range of tones in our image. Slide the Input Black control to the right control until it touches the edge of the visible graph. Then, slide the White Input to the left, until it touches the edge of the visible graph. Shifting the Gamma will then redistribute the midtones between the white and black points. The image below shows how this basic adjustment can improve the image by darkening the blacks to true black, raising the highlights to pure white, and brightening the overall image with a Gamma shift.
![image32](image32.png)

![image33](image33.png)

There are also two triangle controls below the gradient, representing the **Output Black** (black triangle) and **Output White** (white triangle). Shifting these will reduce the contrast in the image, by reducing the intensity of the black point or white point of the image. This can be useful for creating a flat image in preparation for applying final grading adjustments. The image below shows how adjusting the Output Black and Output white affects our result.
![image34](image34.png)

![image35](image35.png)
**Controls**
| •   | **Input Black:** Sets pure black in the image to the selected value. Any tones below the selected value will be clipped to pure black. Linked to the black triangle below the graph. |
|-----|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Input White:** Sets pure white in the image to the selected value. Any tones above the selected value will be clipped to pure white. Linked to the white triangle below the graph. |
|-----|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Gamma:** Redistributes the midtones between the defined input black and input white. Adjusting Gamma to the left will brighten the midtones, and adjusting it right will darken the midtones. Linked to the grey triangle below the graph. |
|-----|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Output Black:** Offsets the black point from 0.0 to the selected value.This is useful for lightening shadow areas of the image. Linked to the black triangle below the gradient. |
|-----|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Output White:** Offsets the white point of the image from 1.0 to the selected value. This can be beneficial for reducing the brightness of the highlights in your image. Linked to the white triangle below the gradient. |
|-----|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
Pro Skin Retouch
Apply realistic and subtle post-production make-up to your actors, with fine control over skin color, detection thresholds, skin treatment and highlight glow.
Skin retouching has three distinct sections. **Skin Detection** is used to define the area to be processed. This area is called the skin matte. **Skin Treatment** contains the main controls for adjusting the amount of processing applied to the skin matte. **Glow** is used to add a subtle glow to the skin area, to soften it.
**Skin Detection**
HitFilm will automatically try to select common skin tones. Adjusting the settings below will allow you to ensure that all skin tones are selected, regardless of what color shifts or lighting is present in your footage.
| •   | **Skin Color:** Sets the base color for skin detection. This should be adjusted based on the subject's skin color, by dragging the eyedropper onto a typical portion of the subject's skin in the viewer. |
|-----|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Brightness Threshold:** Limits the skin detection based on brightness. Higher values will include a wider range of highlights and shadows in the selection. This can be useful for selecting skin in shots with uneven lighting, but higher values also make it easier for unwanted areas of the frame to be included in the skin matte. |
|-----|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Chroma Threshold:** The skin detection is performed in the YUV color space. The chroma threshold defines the distance around the selected color used to create the detection circle. Increasing this setting includes a wider chromatic range in the selection, which can also easily begin to select unwanted areas of the frame. This setting shuld be kept at the lowest value that is acceptable for your footage. |
|-----|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Softness:** Applies a feather to the edge of the skin matte, to more naturally blend it with the rest of the frame. |
|-----|-----------------------------------------------------------------------------------------------------------------------|
| •   | **Elliptical Deformation:** Adjusts the shape of the YUV detection circle into an ellipse, which is a more optimized shape for skin detection. |
|-----|------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Blur Selection:** Blurs the resulting skin matte. |
|-----|-----------------------------------------------------|
**Skin Treatment**
These controls define how the area inside the skin matte is modified.
| •   | **Smooth:** Smoothes the skin by applying a blur within the area of the skin matte. |
|-----|-------------------------------------------------------------------------------------|
| •   | **Edge Threshold:** The skin treatment attempts to retain edge detail while smoothing the skin. The edge threshold determines how much detail is retained. |
|-----|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Saturation:** Adjusts the color intensity of the skin. A subtle saturation boost often creates a healthy appearance. |
|-----|------------------------------------------------------------------------------------------------------------------------|
| •   | **Exposure:** Adjusts the exposure within the skin matte. Since human faces are the most common subject of video shots, this allows you to easily highlight underlit skin, and draw the viewer's eyes to your subject. |
|-----|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
**Glow**
| •   | **Brightness:** Adjusts the strength of the glow. Subtle use is recommended for average shots, but higher values can also be useful for creating elf-glow effects. |
|-----|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Threshold:** Applies a threshold to the skin. Higher thresholds reduce the amount of skin used to generate the glow. |
|-----|------------------------------------------------------------------------------------------------------------------------|
| •   | **Radius:** Higher radius values will increase the size of the glow, creating a softer, more diffuse result. |
|-----|--------------------------------------------------------------------------------------------------------------|
| •   | **Colorize:** The glow can be tinted towards a specific color using the color picker.If you want to tint the glow away from normal skin color, to give it a sickly green tinge or an ethereal blue tint, for example, you could select those colors here. |
|-----|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
**View**
Switching between these view modes makes it easier to adjust the skin detection settings.
| •   | **Final Result:** This option shows the processed skin composited back onto your source layer, so you can see the exact results of the effect. |
|-----|------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Skin Matte:** Shows a greyscale representation of the skin matte, so you can see exactly what areas are selected. White indicates selected areas, black indicates unselected areas, and grey indicates areas of partial selection. The darker a grey area is, the less effect the Skin Treatment settings will have in that area. |
|-----|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Skin:** Isolates the selected area and hides all parts of the layer that are outside of the skin matte. |
|-----|-----------------------------------------------------------------------------------------------------------|
White Balance
If your video was shot with incorrect white balance, or has an undesirable color shift, this effect can help to correct the problem. Use the color pipette to select a part of the video that should be white (or neutral grey) and the layer will be corrected.
In the example below, the white balance has been set to the frames of the sunglasses. The first image is the original, with an overly warm, yellowish appearance, while the second image shows the corrected white balance.
![image17](image17-1.png)

![image36](image36.png)

**Color**

Color grading effects are for giving your project a unique visual style.
See also [Color Correction](http://hitfilm.com/reference/hitfilm-pro/color.htm#hmpopupDiv).
Bleach Bypass
Simulates the harsh, high contrast look of bleach bypass film processing. Often used for war movies.
![image37](image37.png)
Cine Style
Using an s-curve shift, cine style creates a cinematic, Hollywood-style look. It is a fast method for achieving a professional, high quality finish. While it offers a rapid grade, it still provides controls for fine tuning the appearance.
![image38](image38.png)

![image39](image39.png)
Cine style includes built-in grain, vignette and letterboxing features. These can be turned on or off depending on the desired look.
The **s-curve** property adjusts the contrast, while the **color adjustment** properties determine the effect of the color shift. The defaults push towards the orange-and-teal palette popular in Hollywood blockbuster filmmaking.
Classic Cine Style
This effect is all about recreating retro film looks. It includes several presets and can also be fully customized. Here's an example of a preset recreating the look from 1950 film Gentlemen Prefer Blondes:
![image40](image40.png)
Basic contrast is controlled with the built-in **s-curve** adjustment and **exposure** and **saturation** can be easily adjusted.
The film **grain** effect is integrated into classic cine style, applying a range of procedural grains based on 8mm, 16mm and 32mm film stocks.
The red, green and blue channels can be adjusted individually and **letterbox** and **vignette** controls are also included.
Color Cycle
Color cycle loops the color palette. It includes numerous presets for quickly generating specific looks, such as this hue cycle:
![image41](assets/image41.png)
The **input phase** is used to determine which channel from the source is used to map through the color cycle.
Adjusting the **phase shift** will cause the colors to cycle. Each color can be adjusted individually, including adjusting its **alpha** transparency. This can therefore be used to generate mattes based on specific color ranges.
Color Map
The color map effect can be used to apply a color range from one layer to another layer. This is most commonly used with a color gradient.
In the following example this color gradient is used:
![image42](image42.png)
The image below shows the result of using the color map effect with the color gradient above.
The top image is the original, ungraded shot. The middle image shows the full effect of the color map, with the original colors mapped to the new blue gradient. The bottom image shows the color mapped version blended back onto the original to create an appealing color grade.
![image43](image43.png)
In the color map properties you first need to select the **color map source**. This can be any other layer on your timeline.
The **X axis** and **Y axis** property groups define how the color map source is mapped onto the layer.
In the above example, using the **luminance** channel for the X axis results in the gradient's colors being sampled from right to left, starting with the brightest end of the gradient. The Y axis in this case has no effect as the colors in the gradient are uniform from top to bottom.
Color Phase
Each color channel can be phased, shifting it to a different color range.
Color Vibrance
This effect is ideal for adding color to greyscale, procedural effects such as particles and textures.
Here's a grayscale planet created using a combination of fractal noise and sphere effects inside HitFilm:
![image44](image44.png)
Here's the same shot with color vibrance applied:
![image45](image45.png)
Color vibrance is particularly effective at retaining detail in bright areas without creating excessive bloom.
The strength of the **vibrancy** and the **luminance preservation** can be adjusted, as can the **color** and **phasing** of the effect.
Day for Night
A quick way to convert a shot filmed in the day to having the appearance of being filmed at night.
Applies a gradient based on the **Horizon** property, with separate controls for the **near** and **far** areas.
![image46](image46.png)
Duo Tone
Creates a two tone look based on two specified colors.
![image47](image47.png)
Threshold is used to adjust the location color split in the image's brightness scale, while softness is used to adjust the overall contrast.
Grading Transfer
Matches the look of a layer to another layer. This is a quick way to grade based on an existing source.
The transferred grade can then be further customized, either globally or specific to the shadows, mid-tones and highlights.
**Brightness shift** affects how much of the source's brightness is transferred, while **chrominance shift** affects how much of the source's color is transferred.
Hue Colorize
Applies a new hue to the layer,.
![image48](image48.png)
Hue Shift
Moves the entire color spectrum of the layer through different hues.
![image49](image49.png)
Invert
Inverts the colors.
![image50](image50.png)
LUT
LUT files are used to transform color values, which helps to ensure accurate color correction across multiple software and hardware setups. The LUT effect can import .cube LUT files.
LUT also provides a powerful way to provide a one-click grade, simulating specific film stocks and processing techniques. Applying a LUT to flat footage can produce high quality results very quickly.
Take a look at this comparison:
![image51](image51.png)
On the left is the original footage, which was purposely shot to be 'flat', providing a neutral starting point for the grade.
The middle image is using a LUT designed to mimic the look of KODACHROME film. The only additional alteration I've made is to slightly reduce the saturation. In about 10 seconds I went from a basic flat look to a highly dramatic and filmic grade. [Find out more about KODACHROME and grab the LUT here.](https://frankglencairn.wordpress.com/2014/01/15/everything-looks-better-on-kodachrome-k-tone-lut/)
The image on the right is using a Kodak 2393 emulation LUT, Again, I'm achieving a good film look with literally a couple of clicks, and note how different this look is to the KODACHROME. [You can download several film emulation LUTs and find some great behind-the-scenes info here.](http://juanmelara.com.au/print-film-emulation-luts-for-download/)
Shadows & Highlights
Provides fine control over the contrast and sharpness of a layer.
![image52](image52.png)
Three Strip Color
Simulates the three strip color film process commonly used in the early days of color film, resulting in richer, deeper colors.
![image53](image53.png)
Two Strip Color
Simulates the two strip color film process. More information on the process can be found [in this article on Wikipedia](http://en.wikipedia.org/wiki/Technicolor).
Vibrance
Adds pop to your image, emphasizing edge detail by increasing local contrast.
![image54](image54.png)
Vignette
Adds a colored overlay to the edges of the layer. You can customize the color, shape and softness of the vignette.
![image55](image55.png)
Vignette Exposure
This alternate vignette effect adjusts the exposure of the edges of the frame, instead of applying an overlay. This can produce a subtler and more natural vignetting result.
The vignette can also be pushed brighter, which creates a halo effect or can be used to reduce the effects of unwanted vignetting in the source footage.

**Depth**

The depth effects can aid in creating the illusion of depth when blending 2D layers with 3D models or 3D effects. HitFilm also
Depth Mask
Depth Mask can be applied to a 2D layer to mask the layer based on the depth of another layer on the same timeline. For example, you may want a video layer to intersect with a 3D model that you have imported. Normally this would require that the model be set to 3D unrolled, which prevents you from applying effects to the model. But if you apply a Depth Mask to the video, then select the 3D model as the depth layer, they can intersect while still retaining their 2D qualities.
| •   | **Depth Layer:** Select the layer to be used as the depth source. If a video or image is chosen, the color data will be used as a depth map. If a 3D model or particle layer is selected, the Z-depth data of the layer will be used. |
|-----|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Invert:** Inverts the depth map. |
|-----|------------------------------------|
| •   | **Softness:** Feathers the depth map. This will be particularly noticeable where the layers appear to intersect. |
|-----|------------------------------------------------------------------------------------------------------------------|
| •   | **Depth Shift:** Adjusts the apparent depth of the depth layer, in relation to the layer the effect is applied to. Positive values will move it closer to the camera, and negative values will move it farther away. Note that the actual position of the Depth Layer is unaffected. |
|-----|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
Depth Matte
Depth Matte creates a greyscale depth map, based on the depth of another layer on the same timeline. For example, you could apply Depth Matte to a grade layer, then select a 3D model layer as the Depth Layer to generate a greyscale depth map of the 3D layer's contents.
| •   | **Depth Layer:** Select the layer to be used as the depth source. If a video or image is chosen, the color data will be used as a depth map. If a 3D model or particle layer is selected, the Z-depth data of the layer will be used. |
|-----|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Invert:** Inverts the depth map. |
|-----|------------------------------------|
| •   | **Softness:** Feathers the depth map. This defines the total distance between the foreground (black and background (white) of the map. |
|-----|----------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Depth Shift:** Adjusts the apparent depth of the depth layer, in relation to the layer the effect is applied to. Positive values will move it closer to the camera, and negative values will move it farther away. Note that the actual position of the Depth Layer is unaffected. |
|-----|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

**Distort**

The Distort effects are used to change the shape and behaviour of a layer.
Bulge
Creates the illusion of a bulging shape pushing through the layer.
You can choose from multiple shapes and adjust the size and shape of the bulge.
![image56](image56.png)
Chromenator
Creates the appearance of liquid metal.
![image57](image57.png)
Derez (VGHS)
Custom-built for Freddie Wong's Video Game High School web series. Creates a digital glitching appearance.
![image58](image58.png)
Displacement
Shifts the pixels in particular directions according to the displacement source. This can create excellent invisibility and other distortion effects.
You can select the source layer and source channels, plus adjust the strength of the displacement.
![image59](image59.png)
Energy Distortion
Distorts your footage based on a procedurally generated fractal pattern. You can adjust the appearance of the distortion using the controls.
![image60](image60.png)
| •   | **Distortion:** Adjusts the intensity of the distortion applied to the layer. |
|-----|-------------------------------------------------------------------------------|
| •   | **Scale:** Sets the scale of the distortion |
|-----|---------------------------------------------|
| •   | **Diffusion Bias:** Set the amount of the image that is affected by diffusion blurring. Increasing the setting will make the blur more prevalent. |
|-----|---------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Diffusion Strength:** Sets the strength of the blur in the areas affected by diffusion |
|-----|------------------------------------------------------------------------------------------|
| •   | **Distortion Rotation:** Sets the angle in which the distortion is applied. |
|-----|-----------------------------------------------------------------------------|
| •   | **Distort Single Axis:** Enabling this option applies the distortion in a single direction. The specific angle used can be set with the Distortion Rotation setting above. |
|-----|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
Animation
By default the Energy Distortion is animated. You can set the details of the movement within the effect here.
| •   | **Wind Direction:** Sets the direction of the movement |
|-----|--------------------------------------------------------|
| •   | **Wind Speed:** Sets the speed of the movement along the axis determined in the Wind Direction, by altering the position of the noise. Higher values will create more movement in the distortion. |
|-----|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Noise Speed:** Sets the speed of the movement of the fractal noise the distortion is based on. This speed alters the shape of the noise, while the Wind Speed property affects its position. |
|-----|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
Noise
| •   | **Seed:** Acts as a randomizer for the shape of the noise. Each seed value sets a unique starting shape for the procedurally generated noise. |
|-----|-----------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Interpolation:** Provides options for how the noise is interpolated. **Linear** Interpolation uses the simplest path to connect points in the rectilinear grid the effect is based on. Cubic interpolation uses smoother paths to interpolate the grid. Neither option is better than the other, they just provide different options for the effect. |
|-----|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
Transform
Multiple layers of fractal noise are combined to create the final noise that the distortion is based on. The Transform controls adjust the primary noise, while the Sub Settings alter the sub levels of noise that add detail to the distortion.
| •   | **Position:** Sets the position of the primary fractal noise the distortion is based on. |
|-----|------------------------------------------------------------------------------------------|
| •   | **Use Layer:** You can select another layer on your timeline, to parent the position of the distortion to that layer |
|-----|----------------------------------------------------------------------------------------------------------------------|
| •   | **Rotation:** Sets the rotation of the primary fractal noise |
|-----|--------------------------------------------------------------|
| •   | **Axis Scale X:** Alters the aspect ratio of the primary fractal noise by changing its scale along the X axis. Higher values will stretch the distortion horizontally. |
|-----|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Axis Scale Y:** Alters the aspect ratio of the primary fractal noise by changing its scale along the Y axis. Higher values will stretch the distortion vertically. |
|-----|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
Sub Settings
| •   | **Sub Levels:** Sets the number of sub levels that are used to calculate the distortion. Higher levels create greater detail in the distortion. |
|-----|-------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Influence:** Controls the intensity with which the sub levels alter the primary noise. |
|-----|------------------------------------------------------------------------------------------|
| •   | **Scale:** Sets the scale of the sub levels, thus impacting the size of the detail added by the additional sub levels. |
|-----|------------------------------------------------------------------------------------------------------------------------|
| •   | **Rotation:** Alters the angle of the sub levels which are laid over the primary noise. |
|-----|-----------------------------------------------------------------------------------------|
| •   | **Offset:** Sets the position of the sub levels in relation to the primary noise position. |
|-----|--------------------------------------------------------------------------------------------|
| •   | **Center Subscale:** Enabling this option links the center of all subscale layers, so they stay aligned when offset using the above control. |
|-----|----------------------------------------------------------------------------------------------------------------------------------------------|
Fluid Distortion
Distorts your footage based on a procedurally generated fractal pattern. You can adjust the appearance of the distortion using the controls.
![image61](image61.png)
| •   | **Distortion:** Adjusts the intensity of the distortion applied to the layer. |
|-----|-------------------------------------------------------------------------------|
| •   | **Scale:** Sets the scale of the distortion |
|-----|---------------------------------------------|
| •   | **Diffusion Bias:** Set the amount of the image that is affected by diffusion blurring. Increasing the setting will make the blur more prevalent. |
|-----|---------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Diffusion Strength:** Sets the strength of the blur in the areas affected by diffusion |
|-----|------------------------------------------------------------------------------------------|
| •   | **Distortion Rotation:** Sets the angle in which the distortion is applied. |
|-----|-----------------------------------------------------------------------------|
| •   | **Distort Single Axis:** Enabling this option applies the distortion in a single direction. The specific angle used can be set with the Distortion Rotation setting above. |
|-----|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
Animation
By default the Fluid Distortion is animated. You can set the details of the movement within the effect here.
| •   | **Wind Direction:** Sets the direction of the movement |
|-----|--------------------------------------------------------|
| •   | **Wind Speed:** Sets the speed of the movement along the axis determined in the Wind Direction, by altering the position of the noise. Higher values will create more movement in the distortion. |
|-----|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Noise Speed:** Sets the speed of the movement of the fractal noise the distortion is based on. This speed alters the shape of the noise, while the Wind Speed property affects its position. |
|-----|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
Noise
| •   | **Seed:** Acts as a randomizer for the shape of the noise. Each seed value sets a unique starting shape for the procedurally generated noise. |
|-----|-----------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Interpolation:** Provides options for how the noise is interpolated. **Linear** Interpolation uses the simplest path to connect points in the rectilinear grid the effect is based on. Cubic interpolation uses smoother paths to interpolate the grid. Neither option is better than the other, they just provide different options for the effect. |
|-----|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
Transform
Multiple layers of fractal noise are combined to create the final noise that the distortion is based on. The Transform controls adjust the primary noise, while the Sub Settings alter the sub levels of noise that add detail to the distortion.
| •   | **Position:** Sets the position of the primary fractal noise the distortion is based on. |
|-----|------------------------------------------------------------------------------------------|
| •   | **Use Layer:** You can select another layer on your timeline, to parent the position of the distortion to that layer |
|-----|----------------------------------------------------------------------------------------------------------------------|
| •   | **Rotation:** Sets the rotation of the primary fractal noise |
|-----|--------------------------------------------------------------|
| •   | **Axis Scale X:** Alters the aspect ratio of the primary fractal noise by changing its scale along the X axis. Higher values will stretch the distortion horizontally. |
|-----|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Axis Scale Y:** Alters the aspect ratio of the primary fractal noise by changing its scale along the Y axis. Higher values will stretch the distortion vertically. |
|-----|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
Sub Settings
| •   | **Sub Levels:** Sets the number of sub levels that are used to calculate the distortion. Higher levels create greater detail in the distortion. |
|-----|-------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Influence:** Controls the intensity with which the sub levels alter the primary noise. |
|-----|------------------------------------------------------------------------------------------|
| •   | **Scale:** Sets the scale of the sub levels, thus impacting the size of the detail added by the additional sub levels. |
|-----|------------------------------------------------------------------------------------------------------------------------|
| •   | **Rotation:** Alters the angle of the sub levels which are laid over the primary noise. |
|-----|-----------------------------------------------------------------------------------------|
| •   | **Offset:** Sets the position of the sub levels in relation to the primary noise position. |
|-----|--------------------------------------------------------------------------------------------|
| •   | **Center Subscale:** Enabling this option links the center of all subscale layers, so they stay aligned when offset using the above control. |
|-----|----------------------------------------------------------------------------------------------------------------------------------------------|
Heat Distortion
Applies automatic heat distortion with built-in displacement and diffusion. The behavior can be adjusted for faster or slower movement.
![image62](image62.png)
| •   | **Scale:** Sets the scale of the distortion |
|-----|---------------------------------------------|
| •   | **Distortion:** Adjusts the intensity of the distortion applied to the layer. |
|-----|-------------------------------------------------------------------------------|
| •   | **Diffusion Bias:** Set the amount of the image that is affected by diffusion blurring. Increasing the setting will make the blur more prevalent. |
|-----|---------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Diffusion Strength:** Sets the strength of the blur in the areas affected by diffusion |
|-----|------------------------------------------------------------------------------------------|
| •   | **Distortion Rotation:** Sets the angle in which the distortion is applied. |
|-----|-----------------------------------------------------------------------------|
| •   | **Distort Single Axis:** Enabling this option applies the distortion in a single direction. The specific angle used can be set with the Distortion Rotation setting above. |
|-----|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
Animation
By default the Energy Distortion is animated. You can set the details of the movement within the effect here.
| •   | **Wind Direction:** Sets the direction of the movement |
|-----|--------------------------------------------------------|
| •   | **Wind Speed:** Sets the speed of the movement along the axis determined in the Wind Direction, by altering the position of the noise. Higher values will create more movement in the distortion. |
|-----|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Noise Speed:** Sets the speed of the movement of the fractal noise the distortion is based on. This speed alters the shape of the noise, while the Wind Speed property affects its position. |
|-----|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
Noise
| •   | **Seed:** Acts as a randomizer for the shape of the noise. Each seed value sets a unique starting shape for the procedurally generated noise. |
|-----|-----------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Interpolation:** Provides options for how the noise is interpolated. **Linear** Interpolation uses the simplest path to connect points in the rectilinear grid the effect is based on. Cubic interpolation uses smoother paths to interpolate the grid. Neither option is better than the other, they just provide different options for the effect. |
|-----|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
Transform
Multiple layers of fractal noise are combined to create the final noise that the distortion is based on. The Transform controls adjust the primary noise, while the Sub Settings alter the sub levels of noise that add detail to the distortion.
| •   | **Position:** Sets the position of the primary fractal noise the distortion is based on. |
|-----|------------------------------------------------------------------------------------------|
| •   | **Use Layer:** You can select another layer on your timeline, to parent the position of the distortion to that layer |
|-----|----------------------------------------------------------------------------------------------------------------------|
| •   | **Rotation:** Sets the rotation of the primary fractal noise |
|-----|--------------------------------------------------------------|
| •   | **Axis Scale X:** Alters the aspect ratio of the primary fractal noise by changing its scale along the X axis. Higher values will stretch the distortion horizontally. |
|-----|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Axis Scale Y:** Alters the aspect ratio of the primary fractal noise by changing its scale along the Y axis. Higher values will stretch the distortion vertically. |
|-----|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
Sub Settings
| •   | **Sub Levels:** Sets the number of sub levels that are used to calculate the distortion. Higher levels create greater detail in the distortion. |
|-----|-------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Influence:** Controls the intensity with which the sub levels alter the primary noise. |
|-----|------------------------------------------------------------------------------------------|
| •   | **Scale:** Sets the scale of the sub levels, thus impacting the size of the detail added by the additional sub levels. |
|-----|------------------------------------------------------------------------------------------------------------------------|
| •   | **Rotation:** Alters the angle of the sub levels which are laid over the primary noise. |
|-----|-----------------------------------------------------------------------------------------|
| •   | **Offset:** Sets the position of the sub levels in relation to the primary noise position. |
|-----|--------------------------------------------------------------------------------------------|
| •   | **Center Subscale:** Enabling this option links the center of all subscale layers, so they stay aligned when offset using the above control. |
|-----|----------------------------------------------------------------------------------------------------------------------------------------------|
Insect Vision
Creates the tiled appearance of a multi-faceted insect eye.
![image63](image63.png)
Magnify
Zooms in on a specific area of the layer. The shape, size and position of the magnification can all be changed.
![image64](image64.png)
Mosaic
Creates a tiled, mosaic appearance by reducing the number of distinct pixels in the layer.
![image65](image65.png)
Smoke Distortion
Distorts your footage based on a procedurally generated fractal pattern. You can adjust the appearance of the distortion using the controls.
![image66](image66.png)
| •   | **Distortion:** Adjusts the intensity of the distortion applied to the layer. |
|-----|-------------------------------------------------------------------------------|
| •   | **Scale:** Sets the scale of the distortion |
|-----|---------------------------------------------|
| •   | **Diffusion Bias:** Set the amount of the image that is affected by diffusion blurring. Increasing the setting will make the blur more prevalent. |
|-----|---------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Diffusion Strength:** Sets the strength of the blur in the areas affected by diffusion |
|-----|------------------------------------------------------------------------------------------|
| •   | **Distortion Rotation:** Sets the angle in which the distortion is applied. |
|-----|-----------------------------------------------------------------------------|
| •   | **Distort Single Axis:** Enabling this option applies the distortion in a single direction. The specific angle used can be set with the Distortion Rotation setting above. |
|-----|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
Animation
By default the Energy Distortion is animated. You can set the details of the movement within the effect here.
| •   | **Wind Direction:** Sets the direction of the movement |
|-----|--------------------------------------------------------|
| •   | **Wind Speed:** Sets the speed of the movement along the axis determined in the Wind Direction, by altering the position of the noise. Higher values will create more movement in the distortion. |
|-----|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Noise Speed:** Sets the speed of the movement of the fractal noise the distortion is based on. This speed alters the shape of the noise, while the Wind Speed property affects its position. |
|-----|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
Noise
| •   | **Seed:** Acts as a randomizer for the shape of the noise. Each seed value sets a unique starting shape for the procedurally generated noise. |
|-----|-----------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Interpolation:** Provides options for how the noise is interpolated. **Linear** Interpolation uses the simplest path to connect points in the rectilinear grid the effect is based on. Cubic interpolation uses smoother paths to interpolate the grid. Neither option is better than the other, they just provide different options for the effect. |
|-----|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
Transform
Multiple layers of fractal noise are combined to create the final noise that the distortion is based on. The Transform controls adjust the primary noise, while the Sub Settings alter the sub levels of noise that add detail to the distortion.
| •   | **Position:** Sets the position of the primary fractal noise the distortion is based on. |
|-----|------------------------------------------------------------------------------------------|
| •   | **Use Layer:** You can select another layer on your timeline, to parent the position of the distortion to that layer |
|-----|----------------------------------------------------------------------------------------------------------------------|
| •   | **Rotation:** Sets the rotation of the primary fractal noise |
|-----|--------------------------------------------------------------|
| •   | **Axis Scale X:** Alters the aspect ratio of the primary fractal noise by changing its scale along the X axis. Higher values will stretch the distortion horizontally. |
|-----|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Axis Scale Y:** Alters the aspect ratio of the primary fractal noise by changing its scale along the Y axis. Higher values will stretch the distortion vertically. |
|-----|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
Sub Settings
| •   | **Sub Levels:** Sets the number of sub levels that are used to calculate the distortion. Higher levels create greater detail in the distortion. |
|-----|-------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Influence:** Controls the intensity with which the sub levels alter the primary noise. |
|-----|------------------------------------------------------------------------------------------|
| •   | **Scale:** Sets the scale of the sub levels, thus impacting the size of the detail added by the additional sub levels. |
|-----|------------------------------------------------------------------------------------------------------------------------|
| •   | **Rotation:** Alters the angle of the sub levels which are laid over the primary noise. |
|-----|-----------------------------------------------------------------------------------------|
| •   | **Offset:** Sets the position of the sub levels in relation to the primary noise position. |
|-----|--------------------------------------------------------------------------------------------|
| •   | **Center Subscale:** Enabling this option links the center of all subscale layers, so they stay aligned when offset using the above control. |
|-----|----------------------------------------------------------------------------------------------------------------------------------------------|
Twirl
Twists the layer around the effect's center point.
![image67](image67.png)
Waves
Creates a corrugated effect. You can also choose another layer as the displacement source and alter the lighting on the bright and dark sides of the wave.
![image68](image68.png)
Witness protection
This is a quick way to obscure an item within a shot, such as a face, number plate or product logo. You can choose between blur or pixelate styles.
![image69](image69.png)

**Generate**

The Generate effects are used to create new visual elements. These can be applied to layers like any other effect.
3D Extrusion
Extruding creates the appearance of 3D depth in a flat 2D layer. This is often used to enhance titles but can be used on any layer.
![image70](image70.png)
3D extrusion can use the 3D lights in your scene. The material behavior of the extrusion can be adjusted in the **Illumination** property group.
For 3D extrusion to cast shadows the layer must also be set to **3D**.
Another layer can be used as an environment map for extruded text. This is effective for creating reflective text or for inheriting some of the lighting in a background plate.
![image71](image71.png)
Audio Spectrum & Audio Waveform
Generate spectrum or waveform patterns based on an audio layer.
Requires a layer containing audio to function correctly.
The appearance of the spectrum and waveforms can be heavily customized, while behavior is determined via the **audio input** controls.
Auto Volumetrics
Generates volumetric lighting effects which can be positioned in 3D. The volumetric rays are based on a source layer.
Often the most effective way to apply auto volumetrics is to a simple plane layer. You can then specify a separate source layer in the **Light source** properties. Applying the effect to a separate plane provides greater flexibility when moving a 3D camera, as the rays can emanate away from the layer boundaries of the source itself.
The light position determines the angle of the rays. You can also link the light position to another layer, such as a light or point layer.
Caustics
Simulates the distortion caused by viewing through a body of water.
Clouds
Generates a moving, randomly generated cloud texture.
![image72](image72.png)
Drop Shadow
Adds a drop shadow to the layer. You can change the scale, distance and appearance of the shadow, or choose to render the shadow without the layer.
![image73](image73.png)
End Credits Crawl
Creates scrolling end credits with automatic formatting and animation, designed to mimic classic feature film credits.
![image74](image74.png)
The effect is split into multiple design elements and automatically reflows text and adjusts the layout depending on the copy you provide. Formatting and layout for element titles, role descriptions and names can be adjusted independently, giving you a lot of flexibility within the core framework.
If you omit titles or roles, the layout will be automatically updated to still make sense. For example, removing roles will reflow the names into a multi-column layout by default, which is useful for crediting a large stunt or VFX team who all share the same role.
Fractal Noise
Generates a range of textures using procedural methods.
![image75](image75.png)
Each fractal method includes a range of properties for customizing the appearance of the effect.
Grid
Creates a grid pattern. You can adjust the spacing and size of the grid lines.
![image76](image76.png)
Letterbox
The fastest and easiest way to add letterboxing to your movie. Presets enable you to quickly pick from standard film aspect ratios.
![image77](image77.png)
Lightswords
See [Lightswords](http://hitfilm.com/reference/hitfilm-pro/lightswords.htm).
Neon Path \[Layer Only\]
A useful tool for creating animated Neon Path effects. You can use a Text Layer or a Mask to define the shape of the effect, and then control the position and movement of the Neon line on the selected path.
Pond Ripple
Creates ripples which expand and distort the layer.
The size and behavior of the ripples can be adjusted.
![image78](image78.png)
Pulp Sci-fi Title Crawl
An instant way to get perfect Star Wars and Flash Gordon-style openings, complete with separate sections for the teaser, main title and the crawl itself.
![image79](image79.png)
The text is entered into the Teaser, Movie Title, Episode Number, Episode Title and Text Crawl properties. Clicking the font 'A' symbol opens a new window for editing the Movie Title and Text Crawl text.
The formatting and animation of the teaser, movie title and text crawl can be adjusted in separate property groups, with the text reflowing automatically to suit the classic pulp look.
The Movie Title can also be switched to use an image instead of text. This can be useful for creating a more authentic appearance when recreating movie logos.
Radio Waves
Creates geometric shapes that can be warped and animated. Shapes can be heavily customized.
![image80](image80.png)
Reflection
A quick and easy way to create a reflection of the layer.
![image81](image81.png)
Sphere
Creates a sphere that reflects its surroundings.
![image82](image82.png)
The sphere can be heavily customized with separate layers for the optional surface texture and environment map.
The **refractive index** property can be used to accurately simulate refraction from real world materials. [A list of common refractive indices can be found on Wikipedia](http://en.wikipedia.org/wiki/List_of_refractive_indices).
Split Screen Masking
Provides a quick way to set up various split screen layouts. Numerous screen layout presets are included which can then be further customized.
**Cuts** determine how many slots are available for input.
**Input layers/frames** is used to link different layers into the effect.
**Border** changes the separation between cuts.
Text
The Text effect lets you quickly generate text on any timeline, including the Editor. To add Text, drag the Text effect from the Effects panel onto a Plane, an image, or a video clip, to add text to that object. Open the controls for the effect in the Controls panel, and then click the A icon displayed to the right of the Text property. This will open the Edit Text dialog, where you can enter the text you wish to add to the layer. Once you are finished editing the text, click the OK button to close the Edit Text dialog and apply the changes. You can then edit the text and further customize the effect in the Controls panel, or directly on the timeline when working in a composite shot.
| •   | **Text:** This is where you edit the contents of the Text effect. Click the "A" icon to open the Edit Text window. You can then enter whatever text you wish the effect to display. |
|-----|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

![image83](image83.png)
| •   | **Cancel:** discards any changes you have entered and closes the Edit Text window. |
|-----|------------------------------------------------------------------------------------|
| •   | **OK:** Confirms the text you have entered and closes the Edit Text window. Once the window closes, the text will be updated on the viewer. |
|-----|---------------------------------------------------------------------------------------------------------------------------------------------|
**Transform**
You can control the alignment and positioning of the Text effect through these controls.
| •   | **Offset From:** Select the position from which the layer movement will be measured. By default the text is **Centered**, but you can also place it in the **Bottom Left**, **Bottom**, **Bottom Right**, **Left**, **Right**, **Top Left**, **Top**, or **Top Right**. |
|-----|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Position Offset:** Sets the distance, in pixels, which the layer is moved from the default position selected in the **Offset From** menu. |
|-----|---------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Rotation:** Sets the rotation of the layer, in degrees. |
|-----|-----------------------------------------------------------|
**Format**
The Format controls allow you to set the details of the text style for the effect.
| •   | **Font:** Select the font to be used, from a list of all fonts installed on your computer. |
|-----|--------------------------------------------------------------------------------------------|
| •   | **Style:** If your selected font includes different styles (Bold, Light, Italic, etc.), you can select your desired style here. |
|-----|---------------------------------------------------------------------------------------------------------------------------------|
| •   | **Alignment:** The text alignment can be adjusted here. You can align the text to **Left**, **Center**, or **Right**, or **Justify** the text to keep both sides aligned |
|-----|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Color:** Allows you to select a font color. |
|-----|-----------------------------------------------|
| •   | **Opacity:** Sets the transparency of the Text, from completely invisible at 0.00 to completely opaque at 1.00. |
|-----|-----------------------------------------------------------------------------------------------------------------|
| •   | **Font Size:** Sets the size of your text. In general, if you want to enlarge your text, it is better to increase the font size rather than increase the layer Scale above 100%. |
|-----|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Line Spacing:** Defines the vertical spacing between each line of text. |
|-----|---------------------------------------------------------------------------|
| •   | **Enable Word Wrap:** Toggles word wrap on and off. Enabling word wrap means that as soon as the text gets too long to fit in a single line, a line break will be created automatically, and a new line is started automatically. |
|-----|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Word Wrap Width:** Defines the width at which word wrap will be implemented. You can create margins in your text layer by setting the Word Wrap Width to a smaller value than the width of the layer the text effect is applied to. For example, if your text is applied to a Full HD layer that is 1920 pixels wide, and you set the Word Wrap Width to 1800, the 120 pixels that remain will be split to create a 60 pixel wide margin on each side of the layer. |
|-----|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Blend:** Determines how the Text is blended with the layer it is applied to. **None** will prevent the layer from being displayed at all, so only the text is visible. **Normal** displays the text over the top of the layer, so both are visible. Details on all the other Blend Mode options can be found on the page about [Compositing With Blend Modes](http://hitfilm.com/reference/hitfilm-pro/blend_modes.htm). |
|-----|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Motion Blur:** Sets the amount of motion blur applied to the layer when its position is animated. |
|-----|-----------------------------------------------------------------------------------------------------|
Tile
A quick and easy way to tile the layer without needing to create duplicates.
![image84](image84.png)
Timecode
Generates a counter showing the current position in time of the layer or timeline.
Wireframe
Renders a line-based representation of a layer. This is particularly effective when applied to 3D models, to create wireframe views that can be highly customized.
**Type**
There are two main types of wireframe:
| •   | **Mesh:** renders the lines around the triangles that make up the 3D model. |
|-----|-----------------------------------------------------------------------------|
| •   | **Grid:** renders a 3D grid of lines, on the surface of the 3D model. The grid can be further customized to adjust the pattern. |
|-----|---------------------------------------------------------------------------------------------------------------------------------|
**Render Mode**
| •   | **All Triangles:** renders the lines for all triangles within the model. |
|-----|--------------------------------------------------------------------------|
| •   | **Front Facing:** renders lines only for surfaces that are facing towards the camera. |
|-----|---------------------------------------------------------------------------------------|
| •   | **Nearest Triangles:** renders lines only for the parts of the model that are visible to camera. |
|-----|--------------------------------------------------------------------------------------------------|
**Material**
| •   | **Solid Color:** creates solid lines of the chosen color. |
|-----|-----------------------------------------------------------|
| •   | **Model Material:** uses the color from the model’s material. |
|-----|---------------------------------------------------------------|
| •   | **Model Material: \* Color** multiplies the color of the model's material by the chosen color. |
|-----|------------------------------------------------------------------------------------------------|
**Illumination**
Wireframe can use 3D lights for illumination. You can choose to use all lights in the composite shot or specific lights.

**Animated Lasers**

Designed to create laser bolts which fire from one point to another. The lasers can be constructed from multiple lines, which can be further manipulated into spirals, expanding the effect to also be useful in motion graphics animation.
![image85](image85.png)
The laser has two **position** points. These interact with the **Location** property, with the laser animating between the two points as the location is increased.
The effect has built-in controls positioning on the X and Y coordinates, plus a slider for depth. Alternatively you can link the start an end points to separate layers on the timeline (such as 3D point layers), which provides more control.
Number of Beams alters the complexity of the beam. Up to 10 separate beams can be added to the effect, each with their own appearance and spiral settings, building up visually exciting shapes which animate together.
Beam properties
Each beam can be colored, with key properties such as **brightness**, **width**, **length** adjusted as required.
**Tail Sca**le causes the beam to taper at its end.
**Color S**hift moves the overall color of the beam towards either the Core Color or the Glow Color. Tail Color Shift does the same but just for the tail end of the beam.
The **Brightness** and **Color Mix Noise** properties introduce a noise texture, breaking up the solidity of the beam.
Spiral properties
Each beam has associated Spiral properties. These are used to twist the beam's straight line into curving spirals.
Increasing the **Radius** warps the line into a spiral shape. **Path Angle** increases the number of spirals.
Each individual beam can be rotated, or the entire combined shape can be rotated in the **Global Controls**.

**Dimension Rift**

Instantly create a wormhole-style rift in space!
![image86](image86.png)
The Dimension Rift effect has several built-in features for easily creating authentic portals:
| •   | Automatically displace the background video as the portal opens |
|-----|-----------------------------------------------------------------|
| •   | A layer can be selected to be visible through the portal |
|-----|----------------------------------------------------------|
| •   | Pre-animated opening, closing and connecting of portals with controllable animation speed |
|-----|-------------------------------------------------------------------------------------------|
| •   | Fine control over 3D wave surface |
|-----|-----------------------------------|
| •   | Create custom shapes |
|-----|----------------------|
Applying the rift
The Dimension Rift effect can be applied directly onto a video or image layer. This will enable it to displace and warp the background as the portal opens, but you will not be able to rotate and position it in 3D, because it is locked to the host layer.
For more flexibility it is recommended that the effect is added to a separate plane layer (see [Creating and using planes)](http://hitfilm.com/reference/hitfilm-pro/plane_layers.htm). This plane layer can then be transformed in 3D (see [Transforming layers in 3D)](http://hitfilm.com/reference/hitfilm-pro/transforming_layers_in_3d.htm), which will also transform the dimension rift. Even when applied to a separate plane layer, the effect can still warp the desired source layer. See the Wall Image property, detailed below.
Wall image
As described above, when applying the effect you may want it to be able to warp a different layer to the host. The Wall Image property is used to define the layer which should be warped.
For example, take an example of a composite shot containing two layers: a live action video clip and a 3D plane. The Dimension Rift is applied to the 3D plane, which is then positioned in 3D space so that the portal is applied to a wall. The Wall Image property is set to the video layer, so that as the portal opens it warps the video.
Shape
The Dimension Rift defaults to a classic oval shape. This can be customized in the Shape group.
The **From Mask** option can be used to select a separate layer to use as the shape. For example, an image or embedded composite shot containing an alpha channel. This makes it easy to create your own custom shapes.
View
This is what is seen through the portal, when it is open.
With the **Image** set to None, the view through the portal is simply a hole cut through the host layer. Setting the Image to another layer will composite that layer inside the portal. Note that it will only be visible if the **Connection** property is increased above 0.00.
The position, depth (Z), rotation and scale of the selected Image can be adjusted as required. Increasing the Z depth will create a greater sense of parallax movement if you move the portal in 3D.
Appearance & Animation
These settings are used to adjust the outline and interior elements of the portal, and how they animate over time.
The Sparks setting is used when the expansion and connection properties are adjusted.
Optional layers
Specific elements of the effect can be turned on and off, which can be useful when creating more complex composites. This lets you render elements individually, providing finer control.
Colors
The Primary color is used on the side of the dimension rift closest to camera. The Secondary color can be glimpsed through the portal when it is open, and represents the portal on the 'other side'. This can be set to be a different color.
Expansion & Connection
The behavior of the dimension rift is controlled with these properties.
**Expansion** animates the portal appearing/disappearing on a surface. This includes displacement warping as it expands, as long as you have selected a **Wall Image**.
With Connection set to 0.00, the portal will be closed, with a rippling, water-like surface. Increasing the Connection will dissolve the rippling surface to reveal the View, as set in the **View** properties.

**Hyperdrive**

Jumping to lightspeed is as easy as dusting crops with this effect, which generates a spray of streaking stars, complete with built-in animation and customization.
![image87](image87.png)
The overall animation is driven by the **Progress** property. At 0% the stars have not yet appeared, and at 100% they have completed their animation past camera.
The color **Temperature** can be adjusted and **Variation** can be added for a less uniform look.
The **Number** and **Size** of stars can be adjusted, while the **Seed** can be used to generate different renderings of the effect.
**Star Blend** determines how the star streaks interact with each other. Add blend tends to look best, with stars intensifying where they overlap.
**Blend with source** changes how the effect is blended with the host layer. When set to None, the stars will be rendered onto transparency, with the host layer no longer visible, which makes it easy to overlay them onto other layers. Alternatively On Top can be used to composite directly onto the host layer.

**Lightswords**

HitFilm provides the most efficient and high quality method for creating lightsword effects, reducing the rotoscoping requirements and automating key visual elements such as the motion blur 'streak'.
![image88](image88.png)
There are six lightsword effects, depending on the needs of your VFX shot.
| •   | Lightsword Ultra (2-Point Auto) provides a rapid method requiring the placing of a point on the hilt and a point on the blade tip. Once these points are rotoscoped to the movement of the lightsword blade, HitFilm will automatically calculate the appropriate motion blur based on the speed at which the blade is moving. The Ultra version of the effect integrates a variety of distortion types into the effect, which can be used to alter the core shape, to alter the glow shape, and to distort the appearance of the background through the effect. |
|-----|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | Lightsword Ultra (4-Point Manual) allows precise positioning, with two points defining the edges of the hilt and two points defining the edges of the blade tip. Precisely positioning each corner gives you full control over the exact shape of the blade on every frame. This can be useful for artificially enhancing the motion blur of the blade movement, to create the classic 'fanning' effect. The Ultra version of the effect integrates a variety of distortion types into the effect, which can be used to alter the core shape, to alter the glow shape, and to distort the appearance of the background through the effect. |
|-----|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | Lightsword (Glow Only) applies the effect's custom glow behavior to any layer, without providing an interface for easy lightsword generation. This is useful for creating other neon and laser effects. The Ultra version of the effect integrates a variety of distortion types into the effect, which can be used to alter the core shape, to alter the glow shape, and to distort the appearance of the background through the effect. |
|-----|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | The three non-Ultra versions of the effects perform a similar roles, but with a simplified set of controls that does not include distortion. |
|-----|----------------------------------------------------------------------------------------------------------------------------------------------|
The effects share the same general properties:
Hilt & tip
The hilt and tip positions can be set inside the effect, or linked to reference layers via the Position menu. This makes it possible to link the shape to auto-tracked points.
The width of the hilt and tip can be set separately, which can be useful for creating perspective on the blade or creating tapered shapes.
Extension
The lightsword extension can be animated to create the 'ignition' animation, whereby the lightsword blade extends out of the hilt, or contracts back in.
Core
The core is the central part of the effect which directly covers the prop blade.
| •   | **Width:** The Width of the core can be adjusted, as a percentage of the width values set in the Tip and Hilt controls above. |
|-----|-------------------------------------------------------------------------------------------------------------------------------|
| •   | **Color:** The core Color should generally be set sightly off white, in the direction of the color that will be used for the glow. |
|-----|------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Feather:** The edges of the core can be softened with the Feather control. |
|-----|------------------------------------------------------------------------------|
| •   | **Stability:** Lowering the Stability causes the core shape to fluctuate in size. |
|-----|-----------------------------------------------------------------------------------|
Distortion
The Core Distortion controls allow you to procedurally alter the shape of the core to create a variety of animated results.
| •   | **Distortion:** Controls the strength of distortion that is applied to the core. |
|-----|----------------------------------------------------------------------------------|
| •   | **Type:** There are four types of distortion available, each of which gives a different result. They are Energy Distortion, Heat Distortion, Liquid Distortion, and Smoke Distortion. |
|-----|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Noise:** The noise that defines the shape of the distortion can be modified using these properties. They correspond to the controls in the standalone Distortion effects. |
|-----|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Animation:** The movement of the noise that defines the shape of the distortion can be modified using these properties. They correspond to the controls in the standalone Distortion effects. |
|-----|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Blend on Top:** enabling this option will apply the glow above the core, potentially altering the core's color. |
|-----|-------------------------------------------------------------------------------------------------------------------|
| •   | **Use in Glow:** enabling this option will adaptively shift the shape of the glow of the effect to match the distortion of the core shape. |
|-----|--------------------------------------------------------------------------------------------------------------------------------------------|
Flicker \[Ultra Only\]
The Flicker controls will affect the movement of the overall effect.
| •   | **Amount:** Controls the amount of flicker applied to the effect. |
|-----|-------------------------------------------------------------------|
| •   | **Probability:** Adjusts how regular the flicker is. Higher probability settings will make a more regular flicker. |
|-----|--------------------------------------------------------------------------------------------------------------------|
| •   | **Frequency:** Adjusts the timing between the flickering, Higher values will increase the speed of the flicker. |
|-----|-----------------------------------------------------------------------------------------------------------------|
| •   | **Seed:** Changing the seed will randomize the pattern of the flicker. |
|-----|------------------------------------------------------------------------|
Inner Glow
Two glows are built-in to the effect. This makes it possible to create an intense inner glow, with a low width so that it is close to the core, and a wider, diffuse, less bright outer glow.
| •   | **Width:** The width of the inner glow can be adjusted, in pixels. |
|-----|--------------------------------------------------------------------|
| •   | **Color:** The inner glow color should generally be set to a bright, vibrant color. |
|-----|-------------------------------------------------------------------------------------|
| •   | **Alpha:** adjusts the transparency of the inner glow layer. |
|-----|--------------------------------------------------------------|
| •   | **Stability:** lowering the stability causes the glow shape to fluctuate in size. |
|-----|-----------------------------------------------------------------------------------|
| •   | **Flicker:** sets the intensity of brightness flicker applied to the glow. This does not alter the shape of the glow. |
|-----|-----------------------------------------------------------------------------------------------------------------------|
| •   | **Falloff:** alters the range over which the glow edges are feathered. Lower numbers will create a harder edge to the glow. |
|-----|-----------------------------------------------------------------------------------------------------------------------------|
| •   | **Mask:** controls whether masks applied to the layer affect the glow. **Disable** will allow the glow to naturally wrap around the mask edges, for a softer result. **Enable** will cut the glow off exactly at the edge of the mask. **Invert** will reveal the glow outside the mask, while removing it inside. |
|-----|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
Distortion
The Inner Glow Distortion controls allow you to procedurally alter the shape of the inner glow to create a variety of animated results.
| •   | **Distortion:** Controls the strength of distortion that is applied to the core. |
|-----|----------------------------------------------------------------------------------|
| •   | **Type:** There are four types of distortion available, each of which gives a different result. They are Energy Distortion, Heat Distortion, Liquid Distortion, and Smoke Distortion. |
|-----|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Noise:** The noise that defines the shape of the distortion can be modified using these properties. They correspond to the controls in the standalone Distortion effects. |
|-----|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Animation:** The movement of the noise that defines the shape of the distortion can be modified using these properties. They correspond to the controls in the standalone Distortion effects. |
|-----|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
Outer Glow
Two glows are built-in to the effect. This makes it possible to create an intense inner glow, with a low width so that it is close to the core, and a wider, diffuse, less bright outer glow.
| •   | **Width:** The width of the outer glow can be adjusted, in pixels. |
|-----|--------------------------------------------------------------------|
| •   | **Color:** The outer glow color can be set to a similar color to the inner glow color, for a traditional look, or to an entirely different color to create a gradient in the glow. |
|-----|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Alpha:** adjusts the transparency of the inner glow layer. |
|-----|--------------------------------------------------------------|
| •   | **Stability:** lowering the stability causes the core shape to fluctuate in size. |
|-----|-----------------------------------------------------------------------------------|
| •   | **Flicker:** sets the intensity of brightness flicker applied to the glow. This does not alter the shape of the glow. |
|-----|-----------------------------------------------------------------------------------------------------------------------|
| •   | **Falloff:** alters the range over which the glow edges are feathered. Lower numbers will create a harder edge to the glow. |
|-----|-----------------------------------------------------------------------------------------------------------------------------|
| •   | **Mask:** controls whether masks applied to the layer affect the glow. **Disable** will allow the glow to naturally wrap around the mask edges, for a softer result. **Enable** will cut the glow off exactly at the edge of the mask. **Invert** will reveal the glow outside the mask, while removing it inside. |
|-----|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
Distortion
The Inner Glow Distortion controls allow you to procedurally alter the shape of the inner glow to create a variety of animated results.
| •   | **Distortion:** Controls the strength of distortion that is applied to the core. |
|-----|----------------------------------------------------------------------------------|
| •   | **Type:** There are four types of distortion available, each of which gives a different result. They are Energy Distortion, Heat Distortion, Liquid Distortion, and Smoke Distortion. |
|-----|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Noise:** The noise that defines the shape of the distortion can be modified using these properties. They correspond to the controls in the standalone Distortion effects. |
|-----|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Animation:** The movement of the noise that defines the shape of the distortion can be modified using these properties. They correspond to the controls in the standalone Distortion effects. |
|-----|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
Path interpolation
During rapid movement the hilt and tip will fan out, creating a trail. Path interpolation is used to create a natural curve along the hilt and tip ends.
Reducing the scale to zero will remove all interpolation, resulting in straight lines drawn at the hilt and tip ends of the blade. Increasing the scale will create interpolation and curved ends.
The Hilt and Tip angles can be used to further customize the interpolated curve at each end of the shape.
Motion Persistence
The 2-point Auto version automatically creates the streaking of a fast-moving lightsword based on the movement of the points. The appearance of the streaking can be customized to match the source footage.
HitFilm automatically attempts to create a natural trail shape based on the movement of the hilt and tip points, based on the expected behaviour of a blade in motion.
The duration of the trail is determined by the motion persistence. Increasing the value will cause the trail to remain visible for more frames, thus creating a larger trail. Reducing the value will create a smaller trail.
Note that motion persistence is restricted by the Auto Scale Persistence properties, if Auto Scale is activated (see below).
Persistence Shift
Persistence Shift adjusts the interpolation in time. This adjusts the trail to be either in front (1.0), behind (0.0) or in the middle (0.5) of the control point positions. At the default of 0.0 this means that on frames containing fast moving blades you should position the control points on the leading edges of the blade.
Auto Scale Persistence
Auto Scale provides additional control over the generation of the persistence trail, determining when the trail is generated. These settings can be used to match the trail to the natural motion blur found in your footage, which may vary depending on your camera settings.
The Speed and Swing thresholds can be used to restrict the activation of motion persistence. Below the thresholds, the shape will be drawn without the trail. This ensures that the blade does not look indistinct when being moved slowly. As soon as the speed and swing thresholds are exceeded, the trail will be generated according to the motion persistence setting.
The Minimum Persistence property generated a trail even if the thresholds are not met. Setting this to 0.0 ensures the blade shape is defined solely by the core, hilt and tip properties. Raising the value will generate a blur trail even during minor movements.
Disabling Auto Scale Motion switches to only using the Motion Persistence property. Therefore the trail will always be generated even during small movements. A high Motion Persistence value combined with Auto Scale turned off will create a long, unnatural trail. Increasing the motion persistence over 180 can create extreme streaking. This isn't suitable for lightsabers but can be an interesting effect in its own right.
Distortion
A noisy, irregular edge can be applied to the shape by increasing Distortion. If Distortion is reduced to 0 the edge will be regular and smooth.

**Geometry**

Geometry effects can be applied to Text layers to modify the text in 3D space. These effects interact directly with HitFilm's 3D lights and cameras, and allow you to create genuine 3D text natively in HitFilm. Geometry effects can be used individually, or in combination.
Bevel
The Bevel effect cuts the edges of a text layer at an angle in relation to the surface of the text. The size and depth of the angle can be adjusted using the controls.
| •   | **Depth:** Sets the depth of the bevel, in pixels |
|-----|---------------------------------------------------|
| •   | **Expansion:** Defines the width of the bevel, and thus how much of the text face will be affected by it. |
|-----|-----------------------------------------------------------------------------------------------------------|
| •   | **Face:** Choose between Back, Front, or Front & Back to determine the direction in which the bevel will be generated. |
|-----|------------------------------------------------------------------------------------------------------------------------|
| •   | **Internal Edges:** This toggle determines whether internal edges of the layer will be affected by the bevel or not. |
|-----|----------------------------------------------------------------------------------------------------------------------|
Extrude
The Extrude effect uses the shape of your Text layer as a source, and stretches it on the Z axis to create a 3D object.
| •   | **Depth:** Sets the depth of the Extrusion, in pixels |
|-----|-------------------------------------------------------|
| •   | **Face:** Choose between Back, Front, or Front & Back to determine the direction in which the Extrusion will be generated. |
|-----|----------------------------------------------------------------------------------------------------------------------------|
| •   | **Internal Edges:** This toggle determines whether internal edges of the layer will be affected by the extrusion or not. |
|-----|--------------------------------------------------------------------------------------------------------------------------|
Rotate
The Rotate effect allows you to adjust or animate the rotation of the characters in the Text layer. The settings you choose will be applied to each character individually, so rather than rotating the entire layer, each letter or character will be turned on its own axes.
| •   | **X:** Rotates the characters on the X axis, which runs from left to right. Imagine running a skewer through each character from left to right. Adjusting this value is equivalent to turning that skewer by a specified number of degrees. |
|-----|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Y:** Rotates the characters on the Y axis, which runs from top to bottom. Imagine running a skewer through each character from top to bottom. Adjusting this value is equivalent to turning that skewer by a specified number of degrees. |
|-----|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| •   | **Z:** Rotates the characters on the Z axis, which runs from front to back. Imagine running a skewer through each character from front to back. Adjusting this value is equivalent to turning that skewer by a specified number of degrees. |
|-----|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

**Gradients & Fills**

A range of gradients and fills are provided. These can be extremely useful when used in conjunction with other effects, such as **color map** or **shatter**.
4-point color gradient
Generates a 4-color gradient. The colors and mixing of the colors can be changed, as can the position of the gradient points.
![image89](image89.png)
Color gradient
Creates a 2-point gradient of color.
![image90](assets/images/image90\.jpg)
Fill color
Simply fills the layer with the selected color. You can choose to blend the color with the original layer to varying amounts.
![image91](assets/images/image91\.jpg)
Radial gradient
Creates a circular color gradient. The size, position and shape of the gradient can all be tweaked.
![image92](assets/images/image92\.jpg)

*From \<<http://hitfilm.com/reference/hitfilm-pro/gradients__fills.htm>\>*

**Grunge**

The grunge effects are a set of effects for creating the appearance of old or damaged video.
Film damage
Simulates the problems caused by a poorly projected film, including grain, stains, dust and scratches, frame shake and flickering.
You can control each of the elements individually to get the exact look you want.
![image93](assets/images/image93\.jpg)
Film grain
Generates a realistic grain based on 8mm, 16mm or 32mm film stock.
Flicker
Introduces a random flickering to the layer. The behaviour of the flicker can be finely customized.
Grain
This effect provides fine control over the size of the grain.
![image94](assets/images/image94\.jpg)
Half tone
Turns the layer into a half tone image, similar to black and white newspaper print.
You can adjust the composition of the half tone dots.
![image95](assets/images/image95\.jpg)
Half tone color
A color variation of the **Half tone** effect.
![image96](assets/images/image96\.jpg)
Jitter
Creates glitches in video playback order, shuffling the order of frames.
Lens dirt
Simulates dirt on the camera lens and in-lens reflection.
![image97](assets/images/image97\.jpg)
The dirt element can be procedurally generated from various **seed** values, or you can use another layer as the dirt source.
The in-lens reflection flaring can be generated from the applied layer or from another source.
**Threshold** and **intensity** determine the visibility of the lens dirt. Higher thresholds will restrict the effect to brighter areas of the frame.
The blur and pivot angle properties adjust the visual style of the flaring. For realistic results these should be kept relatively high.
Noise
The basic noise effect provides a fixed-size noise.
![image98](assets/images/image98\.jpg)
Scan lines
Creates scan lines as seen on some monitor displays when filmed.
![image99](assets/images/image99\.jpg)
Shake
Adds artificial camera shake to the layer. This can be useful for adding shake to explosive effects, or for adding a sense of a handheld camera to a tripod shot.
Stutter
Reduces the number of frames used during playback of the layer, creating the impression of the video momentarily freezing.
TV damage
Simulates the appearance of a badly tuned television signal.
Each element can be customized individually to create the exact look you want.
![image100](image100.png)

*From \<<http://hitfilm.com/reference/hitfilm-pro/grunge.htm>\>*

**

**

**

**

**

**

**

**

**

**

**

![[image-21.png]]