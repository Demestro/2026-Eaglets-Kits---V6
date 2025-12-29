'''
Made by Venu Saathvik Tummalapenta for Eaglets: Robot kits for Kids
Started on November 30th, 2025

Purpose: This library is custom coded to run RGB NeoPixels

How it works:
The data for the NeoPixels is fed at a rate of 800Khz, which is too fast for .high() and .low() commands to be implemented
because they have a lot of CPU overhead, and can be very off. 
So this program utilizes the Programmable I/O (PIO) blocks found on the RP2040 microprocessor, and (currently) uses the configured I/O mapping in order to influence the State Machines, four of them found in the RP2040. These four State Machines have a shared 32 Line Instruction Set, and have 
''' 