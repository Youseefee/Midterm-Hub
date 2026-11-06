[Windows.Media.Ocr.OcrEngine, Windows.Foundation.Diagnostics, ContentType = WindowsRuntime] | Out-Null
[Windows.Graphics.Imaging.BitmapDecoder, Windows.Graphics.Imaging, ContentType = WindowsRuntime] | Out-Null
[Windows.Storage.StorageFile, Windows.Storage, ContentType = WindowsRuntime] | Out-Null
[System.WindowsRuntimeSystemExtensions, System.Runtime.WindowsRuntime, ContentType = WindowsRuntime] | Out-Null

$ocrEngine = [Windows.Media.Ocr.OcrEngine]::TryCreateFromUserProfileLanguages()
if ($null -eq $ocrEngine) {
    $lang = [Windows.Globalization.Language, Windows.Globalization, ContentType = WindowsRuntime]::new("en-US")
    $ocrEngine = [Windows.Media.Ocr.OcrEngine]::TryCreateFromLanguage($lang)
}

$testFile = (Resolve-Path "extracted_content\business_slides\BA_Lecture_3_s2_0.jpg").Path

function Await($asyncOp) {
    return [System.WindowsRuntimeSystemExtensions]::AsTask($asyncOp).GetAwaiter().GetResult()
}

$file = Await ([Windows.Storage.StorageFile]::GetFileFromPathAsync($testFile))
$stream = Await ($file.OpenAsync([Windows.Storage.FileAccessMode]::Read))
$decoder = Await ([Windows.Graphics.Imaging.BitmapDecoder]::CreateAsync($stream))
$bitmap = Await ($decoder.GetSoftwareBitmapAsync())
$ocrResult = Await ($ocrEngine.RecognizeAsync($bitmap))

Write-Output "=== SUCCESSFUL OCR TEXT ==="
Write-Output $ocrResult.Text
