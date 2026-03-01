import asyncio
from bleak import BleakScanner

async def main():
    devs = await BleakScanner().discover(return_adv=True)
    print(devs)
    
asyncio.run(main())