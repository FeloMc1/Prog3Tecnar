class estudiante:
    def __init__(self, Name="Nombre", Lname="Apellido",Mail="Correo",Phone="telefono"):
        self.Name = Name
        self.LName =Lname
        self.Mail =Mail
        self.phone=Phone
        
    def Getinfo(self):
        print(self.Name)