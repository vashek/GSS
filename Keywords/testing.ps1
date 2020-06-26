python keywords.py input.txt T output.txt -t
Write-Host $LastExitCode "  --0 is expected error code"
Start-Sleep -s 5

python keywords.py input1.txt T output.txt -t
Write-Host $LastExitCode "  --0 is expected error code"
Start-Sleep -s 5

python keywords.py inp.txt T output.txt -t
Write-Host $LastExitCode "  --1 is expected error code"
Start-Sleep -s 5

python keywords.py input2.txt T output.txt -t
Write-Host $LastExitCode "  --0  is expected error code"
Start-Sleep -s 5

python keywords.py input3.txt T output.txt -t
Write-Host $LastExitCode "  --0 is expected error code"
Start-Sleep -s 5

python keywords.py binary T output.txt -t
Write-Host $LastExitCode "  --2 is expected error code"
Start-Sleep -s 5

python keywords.py input1.txt B output.txt -t
Write-Host $LastExitCode "  --2 is expected error code"
Start-Sleep -s 5

python keywords.py binary B output.txt -t
Write-Host $LastExitCode "  --0 is expected error code"
Start-Sleep -s 5

python keywords.py binary1 B output.txt -t
Write-Host $LastExitCode "  --4 is expected error code"
Start-Sleep -s 5

python keywords.py binary2 B output.txt -t
Write-Host $LastExitCode "  --0 is expected error code"
