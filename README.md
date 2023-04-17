# Driver assigner

This is a simple tool to assign the best driver to each of the shipments that we need to complete.

## Getting Started

### Prerequisites

you will need python 3.7+ in order to be able to run this project

### Installing

#### 1. Clone repo

Use your favorite git tool to clone the web repository

```bash
git clone https://github.com/elohim-alt/assigner.git
cd assigner
```

#### 2. Add executable permissions to the scripts

MacOS and Linux

```bash
chmod +x scripts/*
```

#### 3. Run setup script

Create the virtual environment and install all the dependencies:

MacOS and Linux

```bash
./scripts/setup.sh
```

Windows

```bash
scripts\setup.bat
```

At this point you should have a venv directory with all the dependencies installed

## Usage

In order to run the project you should have newline separated files, one with the drivers names and one with the
shipments delivery street names, you can find examples of those files under the data folder.
After setup you should be able to run the project with
MacOS and Linux

```bash
./scripts/run.sh <driver_file_path> <shipment_file_path>
```

Windows

```bash
scripts\run.bat <driver_file_path> <shipment_file_path>
```

you should see an output like this:

```bash
Total Suitability Score:  12.0
Shipment Assignments:
john -> 42nd street
bob -> 1st avenue
johnny -> 10nd strt
```

This output represent the maximum suitability score and the pairing of drivers and shipments that maximize the score.
keep in mind that each driver can only be assigned to one shipment and each shipment can only be assigned to one driver.

### Running the tests

In order to run the tests you just need to run the test command
MacOS and Linux

```bash
./scripts/run_tests.sh
```

Windows

```bash
scripts\run_tests.bat
```

### Using venv directly

If you want to use the venv directly (after install) you can activate it with

MacOS and Linux

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate.bat
```

Then you can run the project with

```bash
python main.py <driver_file_path> <shipment_file_path>
```

In order to run the tests simply do

```bash
pytest
```

## Implementation Notes

### Shipment score calculation

The score of each driver-shipment pair is calculated by the following formula:

- If the length of the shipment's destination street name is even, the base suitability score (SS) is the number of
  vowels in the driver’s
  name multiplied by 1.5.
- If the length of the shipment's destination street name is odd, the base SS is the number of consonants in the
  driver’s name multiplied by 1.
- If the length of the shipment's destination street name shares any common factors (besides 1) with the length of the
  driver’s name, the
  SS is increased by 50% above the base SS.

### Assignment algorithm

- Once we calculate the potential score per driver-shipment pair, we get a matrix of scores, we then use the
  Hungarian/Munkres algorithm to find the optimal assignment of drivers to shipments that maximizes the total score.
- Munkres algorithm solves this problem in O(n^3) time, where n is the number of drivers/shipments.
- Given that the Munkres algorithm only works for bipartisan graphs it requires a square matrix as input, we pad the
  matrix with zeros to make it square, this actually happens at the library level.
- The implication of this is that when we have more drivers than shipments, we will have drivers that do not deliver any
  shipments, and when we have more shipments than drivers, we will have shipments that are not delivered. I believe this
  is an adequate behavior since we have the constrain of only delivering one shipment per driver.

### Other design decisions

- I implemented the project in python since I consider it a good language for this kind of application, it is easy to
  read and write, and I saw there where a couple of libraries that I could use for the implementation.
- I decided to use a virtual environment to isolate the dependencies of the project, on my experience this gives a
  better experience as using and it prevent breaking your system setup.
- I implemented the project as a module, since this gives the flexibility to use it as a library in the future if
  needed.
- I choose to type hint all the functions and methods in the project, I consider this a good practice that helps with
  readability and maintainability, also the IDE and other tools work better when they have the information that type
  hinting provides.
- I did not create data classes for the drivers and shipments since this project does not really require any information
  other than the one that was used. Also the input only holds that data, so the structures would be mostly empty.
- I decided to use shell/batch scripts to run the project and the tests since I consider that user friendly and easy to
  use. I actually was inclined to use a Makefile instead since I consider they are great for this kind of application,
  however I have seen that sometimes are not very friendly for windows users.
- I decided to use a library for the Munkres algorithm since it is a well known algorithm. However I extracted in a way
  in which that part of the functionality is isolated and can be easily replaced if needed.