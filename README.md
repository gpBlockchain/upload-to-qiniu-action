# Upload to Qiniu Action

This is a GitHub Action to upload a file to Qiniu.

## Inputs

| Input        | Description                       | Required |
|--------------|-----------------------------------|----------|
| `access_key` | Your Qiniu Access Key             | Yes      |
| `secret_key` | Your Qiniu Secret Key             | Yes      |
| `bucket_name`| Name of your Qiniu bucket         | Yes      |
| `key`        | Key for the file in Qiniu bucket  | Yes      |
| `local_file`  | Local path to the file to upload  | Yes      |

## Example usage

```yaml
- name: Upload to Qiniu
  uses: gpBlockchain/upload-to-qiniu-action@main
  with:
    access_key: ${{ secrets.ACCESS_KEY }}
    secret_key: ${{ secrets.SECRET_KEY }}
    bucket_name: ${{ secrets.BUCKET_NAME }}
    key: ${{ secrets.KEY }}
    local_file: ${{ secrets.LOCALFILE }}
```

Remember to set `ACCESS_KEY`, `SECRET_KEY`, `BUCKET_NAME`, `KEY`, and `LOCAL_FILE` as secrets in your GitHub repository settings.

## How to set secrets

Go to your GitHub repository, click on the "Settings" tab, then click on the "Secrets" section on the left side. Here you can add the above mentioned secrets. Do not expose your secret key and access key publicly.

## Note

The `local_file` is the local path to the file you want to upload. In a GitHub Actions environment, you may need to get your file by checking out your repository, downloading an artifact, or other methods.

This action is using Qiniu Python SDK, for more information you can check Qiniu's official documentation.
