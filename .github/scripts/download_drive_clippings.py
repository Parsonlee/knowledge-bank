import os
import re
import sys
import gdown
import docx

# 云端 Obsidian_Clippings 文件夹 ID
FOLDER_ID = "1Iv4vMKj4gwZLiEml7fG3U22xQxi_woWX"
TARGET_DIR = "Clippings/DailyDoseOfDS"

def convert_docx_to_clean_md(filepath):
    """检测并自动将 Google Docs 导出的 docx 二进制格式转为干净标准的 Markdown"""
    try:
        with open(filepath, 'rb') as f:
            header = f.read(4)
        if header != b'PK\x03\x04':
            return  # 已经是纯文本 md
    except Exception:
        return

    try:
        doc = docx.Document(filepath)
        md_lines = []
        has_parsed_frontmatter = False

        for p in doc.paragraphs:
            text = p.text.strip()
            if not text:
                if has_parsed_frontmatter and (len(md_lines) > 0 and md_lines[-1] != ''):
                    md_lines.append('')
                continue

            # 解析 Frontmatter 元数据
            if not has_parsed_frontmatter and ('title:' in text and 'type:' in text):
                matches = re.findall(r'(\w+):\s*(\"(?:[^\"]|\\.)*\"|\S+)', text)
                if matches:
                    md_lines.append('---')
                    for k, v in matches:
                        md_lines.append(f'{k}: {v}')
                    md_lines.append('---')
                    md_lines.append('')
                    has_parsed_frontmatter = True
                    continue

            style_name = p.style.name if p.style else ''

            if style_name.startswith('Heading 1'):
                md_lines.append(f'# {text}')
                md_lines.append('')
            elif style_name.startswith('Heading 2'):
                md_lines.append(f'## {text}')
                md_lines.append('')
            elif style_name.startswith('Heading 3'):
                md_lines.append(f'### {text}')
                md_lines.append('')
            elif style_name.startswith('List') or text.startswith('•') or text.startswith('-'):
                clean_text = text.lstrip('•- ').strip()
                md_lines.append(f'- {clean_text}')
            else:
                md_lines.append(text)
                md_lines.append('')

        content = '\n'.join(md_lines).strip() + '\n'
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Successfully converted {os.path.basename(filepath)} from docx to Markdown.")
    except Exception as e:
        print(f"Warning: Failed to convert {filepath}: {e}")

os.makedirs(TARGET_DIR, exist_ok=True)
print(f"Downloading files from Google Drive folder ({FOLDER_ID}) into {TARGET_DIR}...")

try:
    gdown.download_folder(id=FOLDER_ID, output=TARGET_DIR, quiet=False, resume=True)
    print("Download completed successfully. Processing files...")

    # 遍历处理所有剪藏 Markdown 文件
    for root, _, files in os.walk(TARGET_DIR):
        for file in files:
            if file.endswith('.md'):
                convert_docx_to_clean_md(os.path.join(root, file))

    print("All files processed successfully.")
except Exception as e:
    print(f"Download process failed: {e}")
    sys.exit(1)
