<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Registration</title>
</head>
<body>
    <form action="process.php" method="POST">

    <label>LastName</label>
    <input type="text" name="ln" required placeholder="Enter Last Name...">

    <label>FirstName</label>
    <input type="text" name="fn" required placeholder="Enter First Name...">

    <label>MiddleName</label>
    <input type="text" name="mn" required placeholder="Enter Middle Name...">

    <label>Email</label>
    <input type="email" name="email" required placeholder="Enter Email...">

    <label>Password</label>
    <input type="password" name="pass" required placeholder="Enter Password...">

    <input type="button" name="reg" value="SUBMIT">

    
</body>
</html>