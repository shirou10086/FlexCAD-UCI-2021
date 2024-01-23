# [DataViz3D: An Novel Method Leveraging Online Holographic Modeling for Extensive Dataset Preprocessing and Visualization](https://arxiv.org/pdf/2401.10416.pdf)

## Abstract
DataViz3D is an innovative online software that transforms complex datasets into interactive 3D spatial models using holographic
technology. This tool enables users to generate scatter plot within a 3D space, accurately mapped to the XYZ coordinates of
the dataset, providing a vivid and intuitive understanding of the spatial relationships inherent in the data. DataViz3D’s userfriendly interface makes advanced 3D modeling and holographic visualization accessible to a wide range of users, fostering new
opportunities for collaborative research and education across various disciplines. This project is hosted at:[DataViz3D Frontpage](https://cadapp-7f2806a069ea.herokuapp.com/login)

## Features
- **3D Object Manipulation**: Users can add and interact with 3D objects like cubes, cylinders, and spheres.
- **Data Visualization**: Facilitates the conversion of data points from CSV files into visual 3D elements in real-time.
- **3d model Editing**: Allows for the modification of properties of 3D objects such as position (x, y, z), color, and more.
- **Local and Server Storage**: Provides options to save the current state locally or on the server.
- **FPS Testing**: Includes functionality to test frames per second (FPS) in the 3D environment.
- **Holographic Display**: Includes functionality to present Holographic display through Holoplay.js on Looking Glass

## Prerequisites
- Web browser with WebGL support.

## Hardware Compatibility
- For our demonstration, we utilized the Looking Glass 32" display. DataViz3D is also compatible with other visualization hardware from Looking Glass Factory that supports holoplay.js.

## Local Installation
1. Clone or download the repository to your local machine.
2. Install flask and run app.py

## Dependencies
- Three.js (included in `/build/three.min.js`)
- jQuery (included in `/w2ui/jquery-3.5.1.min.js`)
- w2ui (included in `/w2ui/w2ui-1.5.min.js` and its corresponding CSS file)

## Usage
- To add objects, click on the 'Add' menu and select the type of object you want to add.
- Select an object to view and edit its properties in the properties panel.
- Import CSV data through the 'upload CSV' option in the 'Application' menu for data visualization.
- Save the current state either locally or on the server using the 'save' option.

## Contributing
Contributions to DataViz3D are welcome. Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature.
3. Commit your changes.
4. Push to the branch.
5. Create a new Pull Request.

## License
DataViz3D is open-source software licensed under the [MIT License](LICENSE).
