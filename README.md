# Odd Faces Detector
Odd Faces Detector is a simple Blender add-on made to make modeling easier by automatically detecting and counting **tris** (3-vertex faces) and **n-gons** (5+ vertex faces) in Edit Mode. It helps you maintain clean topology and avoid geometry issues during modeling, animation, or export.

**NOTE: This add-on is currently untested with older versions of Blender, it has only been tested on 4.5.4 LTS, so feedback is still awaited for older versions.**

## Authors
* Lomica Inside - currently the only developer of this add-on, got some knowledge from the internet though.

## Current Features
* Live count of tris and n-gons while editing
* Two quick-select buttons:
  * **Select Tris**: Highlights all 3-vertex faces
  * **Select N-Gons**: Highlights all faces with 5 or more vertices
* Works seamlessly in Edit Mode
* Simple UI panel in the Sidebar

## Installation
* 1. Download the latest release ZIP from [GitHub Releases](https://github.com/lomicainside/Odd-Faces-Detector/releases).
* 2. Open Blender and go to **Edit > Preferences > Add-ons**.
* 3. Click **Install**, then select the downloaded `.zip` file.
* 4. Enable **Odd Faces Detector** from the list.
* 5. Access the panel in **View3D > Sidebar > Odd Faces Detector**.

## UI Preview
![](blender.gif)

## Usage Tips
* You must be in **Edit Mode** on a mesh object.
* Use the buttons to quickly identify problematic geometry.
* Great for preparing models for subdivision, animation, or game engines.

## Known Issues
* There are no known issues just yet, there might be soon.

## Version History
**Current Version: 0.5**  
* **v0.5:** This is the first public release of Odd Faces Detector. All prior versions were internal development builds and are not published.
