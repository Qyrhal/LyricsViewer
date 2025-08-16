from objects.song import Song 

class SRTGenerator:
    
    @staticmethod
    def generate_srt(self, path_to_lyrics: Path):
        srt_content = ""
        for i, line in enumerate(lyrics.splitlines()):
            srt_content += f"{i + 1}\n"
            srt_content += f"00:00:00,000 --> 00:00:10,000\n"
            srt_content += f"{line}\n\n"
        return srt_content
