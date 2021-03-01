# API

## Run project


```sh
docker-compose -f local.yml build
docker-compose -f local.yml up
```

## Ports
Django - 8000
Vue - 8080

## Django endpoints
Menu endpoints - menus/
Order endpoints - orders/
User endpoints - users/

## Vue urls (depracated)
Today Orders - /
Create Menus - /create-menu
Create Order for a Specific User - /menu/:idUser ``idUser is a int``

## Postman
To test de Django endpoints in a visual way I recommend to set a postman's enviorenment

## Contact

Vinsmoke Mau – [@vinsmokemau](https://twitter.com/vinsmokemau) – mauricio.munguia@makingmex.com

Distributed under the XYZ license. See ``LICENSE`` for more information.

[https://github.com/vinsmokemau/HitmanApp](https://github.com/vinsmokemau/CornershopTest)

## Contributing

1. Create your feature branch (`git checkout -b feature/fooBar`)
2. Commit your changes (`git commit -am 'Add some fooBar'`)
3. Push to the branch (`git push origin feature/fooBar`)
4. Create a new Pull Request