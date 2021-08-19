# Tests Services ITxPT

Project of an embedded software allowing to test the 
[NTP](https://wiki.itxpt.org/index.php?title=S02P02-Time_-_v2.1.1), 
[GNSS](https://wiki.itxpt.org/index.php?title=S02P03-GNSSLocation_-_v2.1.1), 
[AVMS](https://wiki.itxpt.org/index.php?title=S02P06-AVMS_-_v2.1.1) 
and [APC](https://wiki.itxpt.org/index.php?title=S02P07-APC_-_v2.1.1) 
services of the [ITxPT](https://itxpt.org/) standard within the new electric bus fleet of 
[Keolis Métropole Orléans](https://www.keolis-orleans-recrute.com/qui-sommes-nous/).

## What is ITxPT?
Faced with the increase in the number of on-board equipment in public transport, a need to standardize
communications made itself felt.
The [ITxPT](https://itxpt.org/) association was created to facilitate integration and communication between
systems. Its role is to support all players in the public transport market in the deployment of systems
plug and play computing, modular and with full interoperability. 


## Start-up

### Prerequisites

There is no real prerequisite in order to use the project, you can find an .exe of the software so that anyone can open
this tool. 

However, if you still want to modify the code, you will need at least: 

- Python 3
- The library present in the [requirements.txt](https://github.com/LMontalbano/Tests_Services_ITxPT/blob/main/requirements.txt)

### Installation

To install the software on your machine, you just need to either **Clone**
the project, or **Download** it in [ZIP](https://github.com/LMontalbano/Tests_Services_ITxPT/archive/refs/heads/main.zip).

- To **Clone** the project you can run the command
``git clone https://github.com/LMontalbano/Tests_Services_ITxPT.git`` in a terminal.
  

- If you choose to **Download** the project in 
[ZIP](https://github.com/LMontalbano/Tests_Services_ITxPT/archive/refs/heads/main.zip),
go to your **Downloads**, then unzip the folder ``Tests_Services_ITxPT.zip``. 

### Software launch

The path to access the executable file is as follows: ``Tests_Services_ITxPT/App/dist/``, then you can
simply double-click on the file ``Tests_Services_ITxPT.exe``.

You can also launch the software via a terminal:
- ``cd Tests_Services_ITxPT/IHM``
- ``py Tests_Services_ITxPT.pyw``

## Use
Once the software starts, you find yourself in front of this window:


![Alt text](https://github.com/LMontalbano/Tests_Services_ITxPT/blob/main/Docs/app_screenshot.png?raw=true "app_screenshot")

There are different elements on the main window of the software, we will detail them below:

- Two inputs:
  - **Local Address**: The local IP address of the machine
  - **SAE Address**: The IP address of the SAE UC
	

- The Keolis Orléans Métropole logo


- Six buttons:
  - **Test NTP**: Run 5 iterations of the NTP Test
  - **Test GNSS**: Run 5 iterations of the GNSS Test
  - **Test AVMS**: Start the AVMS Test
  - **Cancel Test AVMS**: Allows you to cancel the AVMS test
  - **Test APC**: Run the APC Test (_not implemented yet_)
  - **All Test**: Run 5 iterations of each test one after the other
    

- A display window
	

- The project's github link

## Technologies used
The project is entirely coded in [Python](https://www.python.org/).
 

For the HMI part, the [Tkinter](https://docs.python.org/3/library/tkinter.html) library was chosen.

For the creation of the .exe, the [PyInstaller](https://www.pyinstaller.org/) library was chosen.



## Status/ Versions
The project is under development and is not yet in production.

## Authors
List of [contributors](https://github.com/LMontalbano/Tests_Services_ITxPT/graphs/contributors): 
- Léonard Montalbano ([LMontalbano](https://github.com/LMontalbano))
- Pierre Lagarde ([avouspierre](https://github.com/avouspierre))

## License

This project is licensed ``MIT`` - see the file [LICENSE.md](LICENSE.md) for more information.


