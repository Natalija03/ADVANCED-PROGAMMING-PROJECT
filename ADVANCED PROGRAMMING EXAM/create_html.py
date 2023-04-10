def creator(filepath, table, headline):
    text_file = open(filepath, "w")
    text_file.write('''
    <html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
    body {
    font-family: Arial, Helvetica, sans-serif;
    margin: 0;
    background-image: url('https://www.unicusano.it/blog/wp-content/uploads/2018/03/struttura-del-dna.jpg');
    background-repeat: no-repeat;
    background-attachment: fixed; 
    background-size: 100% 100%;
    margin:0;
    }

    .navbar {
    margin-top: 0px;
    margin-left: 0px;
    margin-right: 0px;
    overflow: hidden;
    background-color: #333;
    }

    .navbar a {
    float: left;
    font-size: 16px;
    margin-top: 0px;
    margin-left: 0px;
    color: white;
    text-align: center;
    padding: 14px 16px;
    text-decoration: none;
    }

    p1 {
    color: aliceblue;
    font-family: 'Courier New', monospace;
    font-weight: lighter;
    font-size: 3vw;
    }

    table {
    font-family: 'Courier New', monospace;
    border-spacing: 0;
    border-collapse: collapse;
    font-size: 1vw;
    color: aliceblue;
    width:100%;
    }
    td, th {
    border: 1px solid #dddddd;
    text-align: left;
    padding: 8px;
    margin:0;
    }
    </style>
    </head>
    <body>
    <div class="navbar">
        <a href="homepage">Homepage</a>
        <a href="active_operations">Active operations</a>
    </div>
    <br>
    <h1 style="color: aliceblue;font-family: 'Courier New', monospace; font-weight: lighter; font-size: 3vw;">''')
    text_file.write(headline)
    text_file.write('''</h1>
    </body>
    </html>''')
    text_file.write(table)
    text_file.close()