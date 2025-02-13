# Automated-Appointment-Scheduler
🤖 Automated appointment platform with CAPTCHA handling and headless browser support.
## Description  
A stealthy automation tool for navigating the appointment system, featuring intelligent wait strategies and anti-detection mechanisms.

```python
# Key Features
- Undetected ChromeDriver integration
- CAPTCHA solving workflow (auto/manual)
- Dynamic element waiting strategies
- Incognito browsing mode
- type selection
- Error recovery system
```

---

## README.md

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Dependencies](https://img.shields.io/badge/dependencies-undetected__chromedriver%20|%20selenium-orange)

Advanced automation solution for appointment scheduling.

## 🚀 Overview

1. **Stealth Initialization** - Headless browser setup
2. **CAPTCHA Handling** - Hybrid manual/auto approach
3. **Form Navigation**:
   - type selection
   - Applicant number selection
4. **Session Management** - Automated cleanup


## 📋 Requirements
```text
undetected-chromedriver==3.5.5
selenium==4.15.2
python-dotenv==1.0.0
```

## ⚙️ Configuration
1. Create `.env` file:
```ini
CHROME_VERSION_MAIN=131  # Match your Chrome version
WAIT_TIMEOUT=60          # Element wait timeout (seconds)
AUTO_CAPTCHA=False       # Enable experimental auto-CAPTCHA
```

2. Update ChromeDriver version in code:
```python
driver = uc.Chrome(options=options, version_main=int(os.getenv('CHROME_VERSION_MAIN', 131)))
```

## 🖥️ Usage
```bash
python automator.py
```

### Runtime Process
1. 4-minute manual CAPTCHA window
2. Automated form navigation:
   - Selects "National - other"
   - Chooses "1 person" option
3. Clean browser exit

## 🔧 Customization

### Modify Visa Options
```python
# Change type selection
OPTIONS = {
    'other': "//*[contains(text(), 'National - other')]",
    'family': "//*[contains(text(), 'Family ')]"
}

# Change applicant number
PEOPLE_OPTIONS = {
    '1': "//*[contains(text(), '1 person')]",
    '2': "//*[contains(text(), '2 people')]"
}
```

### Adjust Timing Parameters
```python
# Modify countdown duration (minutes)
COUNTDOWN_MINUTES = 4
# Change element wait timeout (seconds)
ELEMENT_TIMEOUT = 20
```

## 🚨 Troubleshooting

### Common Issues
1. **Chrome Version Mismatch**  
   ```bash
   chrome://version/ # Check installed version
   ```

2. **CAPTCHA Detection**  
   Enable manual solving mode:
   ```ini
   AUTO_CAPTCHA=False
   ```

3. **Element Not Found**  
   Increase wait timeout:
   ```python
   WebDriverWait(driver, 30).until(...)
   ```

## ⚠️ Important Notes
- Requires Chrome browser installed
- CAPTCHA solving may require human intervention
- Adjust `version_main` to match local Chrome version

## 🌟 Roadmap
- [ ] Appointment slot monitoring
- [ ] SMS/email notifications
- [ ] Proxy rotation system
- [ ] Browser fingerprint randomization

## 🔒 Compliance Notice
```text
This tool is intended for educational purposes only. Use in accordance with 
the platform's terms of service. Check local regulations before 
automating government services.
```

## 🤝 Contributing
1. Install dev requirements:
```bash
pip install pylint pytest
```
2. Follow PEP8 guidelines
3. Submit PR with detailed testing notes

## 📜 License
MIT License - See [LICENSE](LICENSE) for details
```
