# auth
    Открыть url: https://www.saucedemo.com/v1/
    Ввести "standard_user" в "Username"
    Ввести "secret_sauce" в "Password"
    Кликнуть "Login"
    Проверить, что мы перешли на новый url: https://www.saucedemo.com/v1/inventory.html

[//]: # (auth_negative.md)
    Открыть url: https://www.saucedemo.com/v1/
    Ввести "user" в "Username"
    Ввести "user" в "Password"
    Кликнуть "Login"
    Проверить, что мы перешли на новый url: <https://www.saucedemo.com/v1/inventor
    Проверить что горит красный крестик

[//]: # (burger_about.md)
    Открыть url: https://www.saucedemo.com/v1/
    Ввести "standard_user" в "Username"
    Ввести "secret_sauce" в "Password"
    Кликнуть "Login"
    Кликнуть на бургер меню слева
    Кликнуть на "About"
    Проверить что перешли на url https://saucelabs.com/

[//]: # (burger_logout.md
    Открыть url: https://www.saucedemo.com/v1/
    Ввести "standard_user" в "Username"
    Ввести "secret_sauce" в "Password"
    Кликнуть "Login"
    Кликнуть на бургер меню слева
    Кликнуть на "Logout"
    Проверить что вернулись на страницу входа https://www.saucedemo.com/v1/

[//]: # (burger_reset_app.md)

    Открыть url: https://www.saucedemo.com/v1/
    Ввести "standard_user" в "Username"
    Ввести "secret_sauce" в "Password"
    Кликнуть "Login"
    Кликнуть "Add to cart" на первом продукте
    Кликнуть на бургер меню слева
    Кликнуть "Reset App State"
    Кликнуть на крестик(закрыть бургер)
    Кликнуть на корзину
    Проверить что товар убран из корзины

[//]: # (cart_add_product_from_catalog.md)
    Открыть url: https://www.saucedemo.com/v1/
    Ввести "standard_user" в "Username"
    Ввести "secret_sauce" в "Password"
    Кликнуть "Login"
    Кликнуть "Add to cart"
    Кликнуть на корзину
    Проверить что товар в корзине

[//]: # (cart_add_product_from_product_card.md)
    Открыть url: https://www.saucedemo.com/v1/
    Ввести "standard_user" в "Username"
    Ввести "secret_sauce" в "Password"
    Кликнуть "Login"
    Кликнуть на название товара
    Кликнуть "Add to cart"
    Кликнуть на корзину
    Проверить что товар в корзине //*[@class ="cart_item"]

[//]: # (cart_remove_product_through_cart.md)
    Открыть url: https://www.saucedemo.com/v1/
    Ввести "standard_user" в "Username"
    Ввести "secret_sauce" в "Password"
    Кликнуть "Login"
    Кликнуть "Add to cart"
    Кликнуть на корзину
    Кликнуть на "Remove"
    Проверить что товар не в корзине

[//]: # (cart_remove_product_through_product_card.md)
    Открыть url: https://www.saucedemo.com/v1/
    Ввести "standard_user" в "Username"
    Ввести "secret_sauce" в "Password"
    Кликнуть "Login"
    Кликнуть на название товара
    Кликнуть "Add to cart"
    Кликнуть "Remove"
    Кликнуть на корзину
    Проверить что товар не в корзине //*[@class ="cart_item"]

 # filter_low_to_high
    Открыть url: https://www.saucedemo.com/v1/
    Ввести "standard_user" в "Username"
    Ввести "secret_sauce" в "Password"
    Кликнуть "Login"
    Кликнуть dropdown фильтр
    Кликнуть "Price (low to high)" в dropdown фильтре
    Проверить что все цены продуктов в порядке возрастания

[//]: # (filter_high_to_low.md)
    Открыть url: https://www.saucedemo.com/v1/
    Ввести "standard_user" в "Username"
    Ввести "secret_sauce" в "Password"
    Кликнуть "Login"
    Кликнуть dropdown фильтр
    Кликнуть "Price (high to low)" в dropdown фильтре
    Проверить что все цены продуктов в порядке убывания


[//]: # (filter_low_to_high.md)
    Открыть url: https://www.saucedemo.com/v1/
    Ввести "standard_user" в "Username"
    Ввести "secret_sauce" в "Password"
    Кликнуть "Login"
    Кликнуть dropdown фильтр
    Кликнуть "Price (low to high)" в dropdown фильтре
    Проверить что все цены продуктов в порядке возрастания

[//]: # (placing_an_order.md)
    Открыть url: https://www.saucedemo.com/v1/
    Ввести "standard_user" в "Username"
    Ввести "secret_sauce" в "Password"
    Кликнуть "Login"
    Кликнуть "Add to cart"
    Кликнуть на корзину
    Кликнуть на "Checkout'
    Ввести "Max" в "First Name"
    Ввести "Johns" в "Last name"
    Ввести "99019" в "Zip"
    Кликнуть "Continue"
    Кликнуть "Finish"
    Проверить URL завершенного заказа

[//]: # (product_card_navigate_from_image.md)
    Открыть url: https://www.saucedemo.com/v1/
    Ввести "standard_user" в "Username"
    Ввести "secret_sauce" в "Password"
    Кликнуть "Login"
    Кликнуть на картинку товара
    Проверить что ссылка в картинке совпадает с текущим URL

[//]: # (product_card_navigate_from_name.md)
    Открыть url: https://www.saucedemo.com/v1/
    Ввести "standard_user" в "Username"
    Ввести "secret_sauce" в "Password"
    Кликнуть "Login"
    Кликнуть на название товара
    Проверить что ссылка в названии совпадает с текущим URL