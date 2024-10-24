# CarProject - Car simulator
Collage project with python & LabView
## Contents
- [Instalation](#Instalation)
- [QuickStart](#QuickStart) 
- [Activaiton](#Activaiton) 
- [Packages](#Packages)
- [FAQ](#FAQ)
## Instalation
1. Make virtual enviroment
    ```bash
    python -m venv .venv
    ```
2. Active virtual enviroment
    ```bash
    .\.venv\Scripts\activate 
    ```
3. Packages
- [Flask](#https://flask.palletsprojects.com/en/3.0.x/)
4. Install packages
    ``` bash
    pip install -r requirements.txt 
    ```
5. LabVIEW part
Code is written in LabVIEW 2024 Q1 32bit <br>
REST Library is nescessary
* JKI HTTP REST Client by JKI
    ```bash
    https://www.vipm.io/package/jki_lib_rest_client/?utm_source=vipm_desktop
    ```

## QuickStart
* Run python part for development
    ```bash
    python main.py
    ```
* LabVIEW for devlepment
    ```bash
    run ./UI/main.vi
    ```

## Activaiton

## FAQ
1. If u have problems with activation venv
```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```