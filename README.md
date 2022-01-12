# Artemis CSS library

A nice css library to provide pastel elements to include in your website.

version 0.1.5

## CSS class available

### Declinaison of color

Once you know which class you want to use you can add the following ending work to change the color

Here are the color

Term | color | value
--- | --- | ---
`-primary` | <input type="color" value="#F3D250" title="#F3D250" disabled/> | #F3D250
`-secondary` |  <input type="color" value="#90CCF4" title="#90CCF4" disabled/> | #90CCF4
`-secondary-dark` |  <input type="color" value="#5DA2D5" title="#5DA2D5" disabled/>  | #5DA2D5
`-danger` |  <input type="color" value="#F78888" title="#F78888" disabled/>  | #F78888
`-warning` |  <input type="color" value="#ffb347" title="#ffb347" disabled/>  | #ffb347
`-success` |  <input type="color" value="#77dd77" title="#77dd77" disabled/>  | #77dd77
`-white` |  <input type="color" value="#ECECEC" title="#ECECEC" disabled/>  | #ECECEC
`-black` |  <input type="color" value="#000000" title="#000000" disabled/>  | #000000

### Buttons

* **gamer** (ex: gamer, gamer-danger, gamer-secondary, ...)
* **flat** (ex: flat,flat-danger, flat-secondary, ...)
* **reverse-flat** (ex: reverse-flat, reverse-flat-danger, reverse-flat-secondary, ...)
* **neon** (ex: neon, neon-danger, neon-secondary, ...)

<img src="https://github.com/dianedelallee/artemis/blob/master/demo/img/artemis_button.png" alt="button" title="
button" />

### Inputs

* **artemis-input** (ex: artemis-input, artemis-input-danger, artemis-input-secondary, ...)

<img src="https://github.com/dianedelallee/artemis/blob/master/demo/img/artemis_input.png" alt="Input" title="Input" />

### Highlight

work with some span

* **highlight** (ex: highlight, highlight-danger, highlight-secondary, ...)
* **important** (ex: important, important-danger, important-secondary, ...)
* **show** (ex: show, show-danger, show-secondary, ...)

<img src="https://github.com/dianedelallee/artemis/blob/master/demo/img/artemis_highlight.png" alt="hightlighted text"
title="hightlighted text" />

### Link

* **link** (ex: link, link-danger, link-secondary, ...)

<img src="https://github.com/dianedelallee/artemis/blob/master/demo/img/artemis_link.png" alt="link"
title="link" />

### Container

* **artemis-container**
* **artemis-container-shadow**

inside the container, you can also define a title inside a p tag with the class `artemis-container-title`, like that:
```html
<p class="artemis-container-title">
```

To change the the position of the title (which is left by default), you can add the class `right` or `center` to the container
ex: 
```html
<div class="artemis-container right">
    <p class="artemis-container-title"> test de titre</p>
    <p>test</p>
</div>
```

<img src="https://github.com/dianedelallee/artemis/blob/master/demo/img/artemis_container.png" alt="container"
title="container" />

### Alert

* **artemis-alert** (ex: artemis-alert, artemis-alert-danger, artemis-alert-secondary, ...)
* **artemis-alert-shadow** (ex: artemis-alert-shadow, artemis-alert-danger-shadow, artemis-alert-secondary-shadow, ...)

<img src="https://github.com/dianedelallee/artemis/blob/master/demo/img/artemis_alert.png" alt="alert"
title="alert" />

## How to use it?

```shell
npm install artemis-css
```

It will create a node module package. If you are using a scss file you can directly import it like that

```scss
@import "../node_modules/artemis-css/artemis.min.css";
```

Or if you prefer to include it in the head of your html file.

```html

<link href="./node_modules/artemis-css/artemis.min.css" rel="stylesheet">
```
Last solution, you can use the `cdn.jsdelivr` link (don't forget to change the version on this link):
```html
<link href="https://cdn.jsdelivr.net/npm/artemis-css@0.1.5/artemis.min.css" rel="stylesheet">
```

You can now use all the classes provided by the library

## In the next release

* Propose other style for different form components

## Other
[![Rate on Openbase](https://badges.openbase.com/js/rating/artemis-css.svg)](https://openbase.com/js/artemis-css?utm_source=embedded&utm_medium=badge&utm_campaign=rate-badge)
