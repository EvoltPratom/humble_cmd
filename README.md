# Running your scripts after command prompt starts everytime(Only For Windows cause i'm a noob)

Clone the repository in your local system by using
```sh
git clone https://github.com/EvoltPratom/humble_cmd.git
```
Or for users without git installed, 

Enter Powershell
```powershell
wget -o dir_name.zip https://github.com/EvoltPratom/humble_cmd/archive/master.zip
Expand-Archive dir_name.zip -DestinationPath dir_name
cd dir_name\humble_cmd-master
```

```python
python main.py
```
This executes the helper.py file everytime command prompt is launched
You can change the contents of helper.py to execute what ever you want instead

Initially the helper.py file contains a small script to show you a new word and new quote everyday to make your day maybe just a little better

If you want the feature removed run uninstall.py as
```sh
python uninstall.py
```
