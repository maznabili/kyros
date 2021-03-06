import asyncio
import logging
import sys

import pyqrcode

import kyros

logging.basicConfig(level=logging.DEBUG)


async def amain():
    whatsapp = await kyros.Client.create()
    qr_data, scanned = await whatsapp.qr_login()
    qr_code = pyqrcode.create(qr_data)
    print(qr_code.terminal(quiet_zone=1))
    try:
        await scanned
    except asyncio.TimeoutError:
        await whatsapp.shutdown()
        return
    await whatsapp.logout()


if __name__ == "__main__":
    try:
        asyncio.run(amain())
    except KeyboardInterrupt:
        sys.exit()
