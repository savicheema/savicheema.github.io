import subprocess
subprocess.run(["git", "init"])
subprocess.run(["git", "remote", "add", "origin", "git@github.com:savicheema/savicheema.github.io.git"])

subprocess.run(["git", "status"])
key_pressed = input("Press 'y' to continue.")
if key_pressed == 'y':
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", "message"])

    subprocess.run(["git", "push", "-f", "origin", "main"])

