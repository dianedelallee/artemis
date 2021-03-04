# Artemis CSS library

version 0.1.3

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

<img src="https://github.com/dianedelallee/artemis/blob/master/demo/img/artemis_hightlight.png" alt="hightlighted text"
title="hightlighted text" />

### Link

* **link** (ex: link, link-danger, link-secondary, ...)

<img src="https://github.com/dianedelallee/artemis/blob/master/demo/img/artemis_link.png" alt="link"
title="link" />

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

You can now use all the classes provided by the library

## In the next release

* Propose other style for different form components
