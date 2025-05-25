import os
import typer
import requests
import datetime
from tqdm import tqdm
from lib.scraper import InstaDL

app = typer.Typer(help="📥 Instagram Reel and Photo Downloader.\n\n"
                        "Use the `reel` or `photo` command to download media from Instagram.\n"
                        "Supports downloading multiple URLs at once.")

def download_media(url: str, media_type: str, save_folder: str):
    try:
        scraper = InstaDL()
        if media_type == "reel":
            results = scraper.Reel(url)
        elif media_type == "photo":
            results = scraper.Photo(url)
        else:
            raise ValueError("Invalid media type: only 'reel' or 'photo' are supported.")

        folder_name = save_folder if save_folder else datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        folder_path = os.path.join(os.getcwd(), folder_name)
        os.makedirs(folder_path, exist_ok=True)

        for idx, result in enumerate(tqdm(results["url"], desc=f"Downloading {media_type.capitalize()}")):
            file_extension = "mp4" if media_type == "reel" else "jpg"
            file_name = f"{media_type}_{idx + 1}.{file_extension}"
            file_path = os.path.join(folder_path, file_name)

            response = requests.get(result)
            response.raise_for_status()  

            with open(file_path, "wb") as file:
                file.write(response.content)

        typer.echo(f"✅ {media_type.capitalize()} successfully downloaded! Check the '{folder_name}' folder.")
    except Exception as e:
        os.system("clear")
        typer.echo(f"❌ An error occurred while downloading {media_type}: {e}")

@app.command(help="📽️ Download Instagram Reels from one or multiple URLs (wrap them in quotes and separate with commas).")
def reel(
    urls: str = typer.Option(..., "--url", "-u", help="Instagram Reel URL(s) to download. Separate multiple URLs with commas."),
    save_folder: str = typer.Option(None, "--save", "-s", help="Folder name to save the downloaded files.")
):
    for url in urls.split(","):
        download_media(url.strip(), "reel", save_folder)

@app.command(help="📸 Download Instagram Photos from one or multiple URLs (wrap them in quotes and separate with commas).")
def photo(
    urls: str = typer.Option(..., "--url", "-u", help="Instagram Photo URL(s) to download. Separate multiple URLs with commas."),
    save_folder: str = typer.Option(None, "--save", "-s", help="Folder name to save the downloaded files.")
):
    for url in urls.split(","):
        download_media(url.strip(), "photo", save_folder)

if __name__ == "__main__":
    app()
