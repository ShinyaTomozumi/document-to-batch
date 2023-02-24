# document_to_batch
This program creates the source code for a batch template from a design document.

## How to use
The usage is as follows.

1. Copy the documents under the "_sample" folder.
2. Edit "SampleBatchCommand.xlsx" to create a batch design document.
3. On the command line, run "document_to_batch.py".
4. Set parameters as needed.

## Requirement
The environment in which this program operates is as follows.<br/>
It is possible that it will work even if the version is small.<br/>
But no guarantees.<br/>

 - python v3.9

To read the Excel file, install the library with the following command.
```commandline
pip install openpyxl
```

## Options
To use this tool on the command line, use the following options.

| Option | Description                                                                                               |
|--------|-----------------------------------------------------------------------------------------------------------|
| -t     | Required.<br>Set the project type.<br/>The following projects are currently supported<br/><br/> - laravel |
| -i     | Required.<br>Specify the path of the document file to be read.                                            |
| -o     | Optional.<br>Specify the path to which the source code will be written.                                   |
| -doc   | Optional.<br>Specifies the document type.<br/><br/>Support:<br/> - excel<br/><br/>Default:<br/> - excel   |


## Design document
### - Excel
The Excel format is written based on "SampleBatchCommand.xlsx" in the "_sample" folder.
Below is a description of the items from left to right.

| Key         | Description                                                                                                                      |
|-------------|----------------------------------------------------------------------------------------------------------------------------------|
| ID          | Required.<br>Unique batch ID.<br/>Describes in PascalCase format.                                                                |
| Summary     | Required.<br>Here is an overview of the batch.                                                                                   |
| Description | Optional.<br>This is required for web-related programs.<br>When defining a path to be passed as a parameter, prefix it with "_". |
| Timing      | Optional.<br>When to execute the batch.<br/>There is no specific format, but a simple description should be good.                |
| Remark      | Optional.<br>Describe any additional items that should be added that are not listed in the description.　                         |


## Note
I created this program to create a Laravel batch program template based on my batch design document.<br>
In the past projects I have been involved in, I have created batch design documents and templates for my people to implement, which can speed up the man-hours to implement as much as possible.<br>
Thank you!

## Author
* Copyright (c) 2023 Shinya Tomozumi
* Tomozumi System: https://tomozumi-system.com
* Twitter : https://twitter.com/hincoco27