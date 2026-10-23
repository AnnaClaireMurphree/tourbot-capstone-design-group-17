# tourbot-capstone-design-group-17

## About the Project
The goal of this project is to build a mobile telepresence unit that can guide a local or remote visitor through the third floor of Broun Hall. 
The customer is the Auburn University Department of Electrical and Computer Engineering, represented by Dr. Thad Roppel. 
The intended end users are prospective students touring the department, students and visitors with mobility limitations who cannot easily walk 
the route, and remote guests joining a tour from off campus. 
The proposed unit is a differential-drive mobile base carrying a camera and display on a height-adjustable mast. 
It can be driven either by a remote user through a browser client or by a local user through an onboard touchscreen, 
and it uses onboard obstacle sensors and a stored floor plan to avoid collisions and to show both users where it is.

## File Information
### Occupancy Grid
`occupancy_grid_generator` takes information from a .txt file with a format like `test_vectors` and encodes it into a 2D matrix, where a
0 represents movable space, a 1 represents an obstacle, a 2 represents a door, and a 3 represents an open area that should not be blocked.
