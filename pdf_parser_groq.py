import fpdf
import json

# Load the podcast episodes from the JSON file
with open('podcast_episodes.json', 'r') as f:
    podcast_episodes = json.load(f)

# Create a PDF file to store the podcast episodes
pdf = fpdf.FPDF()

# Set the font and font size
pdf.set_font("Arial", size = 12)

# Loop through each podcast episode
for episode in podcast_episodes.values():
    # Check if the number of tokens is less than or equal to 12,000
    if len(episode["tokens"]) <= 12000:
        # Add a new page to the PDF
        pdf.add_page()

        # Write the episode title, source, URL, text, and tokens to the PDF
        pdf.cell(200, 10, txt = episode["title"], ln = True, align = 'L')
        pdf.ln(10)
        pdf.cell(200, 10, txt = episode["source"], ln = True, align = 'L')
        pdf.ln(10)
        pdf.cell(200, 10, txt = episode["url"], ln = True, align = 'L')
        pdf.ln(10)
        pdf.cell(200, 10, txt = episode["text"], ln = True, align = 'L')
        pdf.ln(10)
        pdf.cell(200, 10, txt = str(episode["tokens"][:12000]), ln = True, align = 'L')

# Save the PDF file
pdf.output("podcast_episodes.pdf")
