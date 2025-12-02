---
date created: 2025-08-06
modified: 2025-08-06
---
## Installation
Copy the ffmpeg files to a directory and add the `bin` directory to the Windows Path Environment variable

## Log

## Links
- [VidCoder](applications/video/VidCoder.md)
- [Handbrake](applications/video/Handbrake.md)

## Python script voor conversie naar [[H.265]]
(Is voor verbetering vatbaar, maar doet wat het moet doen)

```Python
import os
from collections import Counter
from datetime import datetime
import pprint

import subprocess
import json


import os
import subprocess
import json
import csv
import shutil
import time
import datetime
import send2trash  # Voeg deze import toe (zorg dat send2trash geïnstalleerd is)

def get_video_codec(file_path):
    command = [
        'D:/OneDrive/Apps/ffmpeg/bin/ffprobe', '-v', 'error',
        '-select_streams', 'v:0',
        '-show_entries', 'stream=codec_name',
        '-of', 'json',
        file_path
    ]
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    try:
        info = json.loads(result.stdout)
        codec = info['streams'][0]['codec_name'] if 'streams' in info and info['streams'] else 'unknown'
    except Exception:
        codec = 'error'
    return codec

def convert_video(input_path, output_path, ext, crf=22):
    """
    Kies conversie-opties op basis van de extensie van het videobestand.
    """
    if ext.lower() == ".avi":
        # Voorbeeld: gebruik NVENC voor avi
        command = [
            'D:/OneDrive/Apps/ffmpeg/bin/ffmpeg', '-i', input_path,
            '-c:v', 'hevc_nvenc',
            '-vf', 'yadif',
            '-cq', str(crf),
            '-c:a', 'copy',
            '-preset', 'slow',
            '-map_metadata', '0',
            output_path
        ]
    elif ext.lower() == ".mts":
        # Voorbeeld: gebruik software encoding voor MTS
        command = [
            'D:/OneDrive/Apps/ffmpeg/bin/ffmpeg', '-i', input_path,
            '-c:v', 'hevc_nvenc',
            '-crf', str(17),
            '-c:a', 'aac',
            '-b:a', '160k',
            '-ac', '2', 
            '-preset', 'slow',
            '-map_metadata', '0',
            output_path
        ]
    elif ext.lower() == ".mpg":
        # Voorbeeld: gebruik software encoding voor MPG
        command = [
            'D:/OneDrive/Apps/ffmpeg/bin/ffmpeg', '-i', input_path,
            '-c:v', 'hevc_nvenc',
            '-vf', 'yadif',
            '-cq', str(22),
            '-c:a', 'aac',        # Verander van 'copy' naar 'aac' voor hercodering
            '-b:a', '128k', 
            '-ac', '1',  # Mono audio
            '-preset', 'slow',
            '-map_metadata', '0',
            output_path
        ]
    else:
        # Standaard: kopieer zonder conversie
        command = [
            'D:/OneDrive/Apps/ffmpeg/bin/ffmpeg', '-i', input_path,
            '-c', 'copy',
            '-map_metadata', '0',
            output_path
        ]
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return result.returncode == 0

def get_metadata(file_path):
    command = [
        'D:/OneDrive/Apps/ffmpeg/bin/ffprobe', '-v', 'error',
        '-show_format', '-show_streams',
        '-print_format', 'json',
        file_path
    ]
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    try:
        metadata = json.loads(result.stdout)
    except Exception:
        metadata = {}
    return metadata

def process_videos_in_directory(directory, output_csv='video_conversion_log.csv'):
    video_extensions = ['.avi', '.mts', '.mpg']  # ['.mp4', '.MTS', '.avi', '.mov', 'MPG', "mpg"]
    log_data = []

    # Definieer de toegestane tijdsperiode
    overwrite_start = datetime.datetime(2025, 8, 1)
    overwrite_end = datetime.datetime(2025, 8, 5, 14, 55)

    for filename in os.listdir(directory):
        print(f"⏩ Verwerken bestand: {filename}")
        if any(filename.lower().endswith(ext) for ext in video_extensions):
            input_path = os.path.join(directory, filename)
            codec = get_video_codec(input_path)
            metadata = get_metadata(input_path)
            converted = False
            output_filename = f"{os.path.splitext(filename)[0]}.mp4"
            output_path = os.path.join(directory, output_filename)

            print(output_path)

            # Controleer of output bestand al bestaat
            if os.path.exists(output_path):
                # Haal de aanmaakdatum van het output bestand op
                created_ts = os.path.getctime(output_path)
                created_dt = datetime.datetime.fromtimestamp(created_ts)
                if not (overwrite_start <= created_dt <= overwrite_end):
                    print(f"⏩ Output bestand bestaat al en valt NIET in de toegestane periode: {output_path}, overslaan.")
                    continue
                else:
                    print(f"⚠️ Output bestand bestaat al, maar valt in de toegestane periode ({created_dt}), wordt overschreven.")
                    print(f"⏩ Verwijderen van bestaand bestand: {output_path}")
                    os.remove(output_path)  # Verwijder het oude bestand voordat

            if codec != 'hevc':
                converted = convert_video(input_path, output_path, os.path.splitext(filename)[1])
                if converted:
                    # Neem bestandsdatums over
                    stat = os.stat(input_path)
                    os.utime(output_path, (stat.st_atime, stat.st_mtime))
                    # Verplaats bronbestand naar de prullenbak
                    send2trash.send2trash(input_path)

            log_entry = {
                'filename': filename,
                'codec': codec,
                'converted': converted,
                'output_file': output_filename if converted else '',
                'metadata': json.dumps(metadata)
            }
            log_data.append(log_entry)

    with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['filename', 'codec', 'converted', 'output_file', 'metadata']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for entry in log_data:
            writer.writerow(entry)

    #print(f"✅ Klaar! Log opgeslagen in: {output_csv}")


if __name__ == '__main__':
    path = r"D:\OneDrive\Afbeeldingen"
    for root, dirs, files in os.walk(path):
        process_videos_in_directory(root)

    pass

```