from huggingface_hub import snapshot_download
snapshot_download(repo_id="tloen/alpaca-lora-7b", cache_dir="./lora")
