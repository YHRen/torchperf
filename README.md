# Convert Current & Pending from NSF/DOE pdf format to NIH docx format

<p align="left">
<a href="https://opensource.org/licenses/BSD-3-Clause"><img alt="License" src="https://img.shields.io/badge/License-BSD_3--Clause-blue.svg"></a>
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>

This code is to extract information from "current and pending" generated through [SciENcv](https://www.ncbi.nlm.nih.gov/sciencv/).
It can also output to the NIH ["Other Support"](https://grants.nih.gov/grants/forms/all-forms-and-formats/other-support-format) docx format.

## Install

```
pip install pypdf python-docx tabulate
git clone github.com/YHRen/convertCP && cd convertCP
```

## Usage

```
python convertCP <your_current_and_pending.pdf> # to convert to plaintext table
python convertCP <your_current_and_pending.pdf> --nih # to convert to NIH docx
```

## Note

This script has been tested on the following C&P version:

```
DOE: SCV C&P(O)S v.2023-1 (rev.01/31/2023)
NIH: OMB No. 0925-0001 and 0925-0002 (Rev. 12/2020 Approved Through 02/28/2023)
```

*DISCLAIMER:* this code is neither supported nor approved by DOE, NSF or NIH. The
author is not responsbile for any damages to the file or computer.

## Known Issues

* DOE/NSF C&P does not contain the field "Name of PD/PI". The NIH output will
  fill this entry as `TODO`.
* For "Status of Support", the program expects "current" or "pending", and
  outputs "current" and "pending". The NIH example suggests terms "Active" and
  "Pending".
* In the case of converting to NIH format:
    - "Person Months" will always use the unit "calendar" month, which DOE/NSF C&P uses.
    - "Overlap" will not be used. NIH requires "Overlap" for Pending projects but not Active projects.
