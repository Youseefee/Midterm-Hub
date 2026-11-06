# PowerShell WinRT OCR script
Add-Type -AssemblyName System.Drawing

[Windows.Media.Ocr.OcrEngine, Windows.Foundation.Diagnostics, ContentType = WindowsRuntime] | Out-Null
[Windows.Graphics.Imaging.BitmapDecoder, Windows.Graphics.Imaging, ContentType = WindowsRuntime] | Out-Null
[Windows.Storage.StorageFile, Windows.Storage, ContentType = WindowsRuntime] | Out-Null

$lang = [Windows.Globalization.Language]::new("en-US")
$ocrEngine = [Windows.Media.Ocr.OcrEngine]::TryCreateFromLanguage($lang)

$testFile = (Resolve-Path "extracted_content\business_slides\BA_Lecture_3_s2_0.png").Path

function Get-OcrText($filePath) {
    $asyncFile = [Windows.Storage.StorageFile]::GetFileFromPathAsync($filePath)
    $file = $asyncFile.GetAwaiter().GetResult()

    $asyncStream = $file.OpenAsync([Windows.Storage.FileAccessMode]::Read)
    $stream = $asyncStream.GetAwaiter().GetResult()

    $asyncDecoder = [Windows.Graphics.Imaging.BitmapDecoder]::CreateAsync($stream)
    $decoder = $asyncDecoder.GetAwaiter().GetResult()

    $asyncBitmap = $decoder.GetSoftwareBitmapAsync()
    $bitmap = $asyncBitmap.GetAwaiter().GetResult()

    $asyncOcr = $ocrEngine.RecognizeAsync($bitmap)
    $ocrResult = $asyncOcr.GetAwaiter().GetResult()

    return $ocrResult.Text
}

$text = Get-OcrText $testFile
Write-Output "=== OCR RESULT FOR SLIDE 2 ==="
Write-Output $text
