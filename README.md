# Black Metal Neovim

![logo](https://github.com/user-attachments/assets/ea628526-a058-4aeb-832f-c99d36d508a0)

The definitive collection of black-metal inspired neovim colorschemes!

This new version is based on the great work done by @cdmill on https://github.com/cdmill/neomodern.nvim. Big hail to him!

If you want to support the project, buy a T-shirt with the logo on [printify](https://black-metal-neovim.printify.me/product/19851229/neovim-graphic-unisex-softstyle-t-shirt-alternative-style-for-music-lovers)!

## Included themes

### Bathory

<img width="450" alt="bathory" src="https://github.com/user-attachments/assets/0999bc6e-b5fb-4d04-842c-733609157004" />

### Burzum

<img width="450" alt="burzum" src="https://github.com/user-attachments/assets/4eca109b-99ce-4127-a27a-cec2f3a94436" />

### Dark Funeral

<img width="450" alt="dark-funeral" src="https://github.com/user-attachments/assets/f35d878c-d7a5-4e61-8897-b6d13be42bed" />

### Darkthrone

<img width="450" alt="darkthrone" src="https://github.com/user-attachments/assets/e6552259-6a1b-4952-bc7e-03be3866c45b" />

### Emperor

<img width="450" alt="emperor" src="https://github.com/user-attachments/assets/6a06f7ab-9315-4942-837b-06fdddfdea16" />

### Gorgoroth

<img width="450" alt="gorgoroth" src="https://github.com/user-attachments/assets/c972574a-a816-44ca-828e-ab672021d38c" />

### Immortal

<img width="450" alt="immortal" src="https://github.com/user-attachments/assets/65f4b381-9faf-4d38-b54d-6011d381dec2" />

### Impaled Nazarene

<img width="450" alt="impaled-nazarene" src="https://github.com/user-attachments/assets/7c3795f5-9ed1-4ca5-9ac5-abe28925d3b6" />

### Khold

<img width="450" alt="khold" src="https://github.com/user-attachments/assets/9ed760e5-76e2-42b7-b969-b708e52ceda1" />

### Marduk

<img width="450" alt="marduk" src="https://github.com/user-attachments/assets/c979f2f1-cb28-4b0f-bdb5-ddaf95034979" />

### Mayhem

<img width="450" alt="mayhem" src="https://github.com/user-attachments/assets/2f3a259d-bcd0-421c-a89e-67e58732f28b" />

### Nile 

<img width="450" alt="nile" src="https://github.com/user-attachments/assets/2b45098f-863d-4a1b-aa97-c3957571e367" />

### Taake

<img width="450" alt="taake" src="https://github.com/user-attachments/assets/8c551eed-e429-4d2b-8727-aea8eac14e04" />

### Venom

<img width="450" alt="venom" src="https://github.com/user-attachments/assets/289d4ac4-0ce8-4a6b-88ff-7da871edfed5" />

## Rationale

Each theme palette is a slight variation of the base one. I picked two accent colors from an album cover for each band.

## Installation

With lazy.nvim:

```lua
-- Using lazy.nvim
{
  "metalelf0/black-metal-theme-neovim",
  lazy = false,
  priority = 1000,
  config = function()
    require("black-metal").setup({
      -- optional configuration here
    })
    require("black-metal").load()
  end,
}
```

## Configuration

There are 14 themes included, each with a light and dark variant. Yes, I know, light variants aren't `TRVE`. Just don't use them if you don't like them.
The light theme is used when `{ variant = "light" }` is passed to `setup(options)` or when `vim.o.background = "light"`.

Default options are given below:

```lua
require("black-metal").setup({
  -----MAIN OPTIONS-----
  --
  -- Can be one of: bathory | burzum | dark-funeral | darkthrone | emperor | gorgoroth | immortal | impaled-nazarene | khold | marduk | mayhem | nile | taake | venom
  theme = "bathory",
  -- Can be one of: 'light' | 'dark', or set via vim.o.background
  variant = "dark",
  -- Use an alternate, darker bg
  alt_bg = false,
  -- If true, docstrings will be highlighted like strings, otherwise they will be
  -- highlighted like comments. Note, behavior is dependent on the language server.
  colored_docstrings = true,
  -- If true, highlights the {sign,fold} column the same as cursorline
  cursorline_gutter = true,
  -- If true, highlights the gutter darker than the bg
  dark_gutter = false,
  -- if true favor treesitter highlights over semantic highlights
  favor_treesitter_hl = false,
  -- Don't set background of floating windows. Recommended for when using floating
  -- windows with borders.
  plain_float = false,
  -- Show the end-of-buffer character
  show_eob = true,
  -- If true, enable the vim terminal colors
  term_colors = true,
  -- Keymap (in normal mode) to toggle between light and dark variants.
  toggle_variant_key = nil,
  -- Don't set background
  transparent = false,

  -----DIAGNOSTICS and CODE STYLE-----
  --
  diagnostics = {
    darker = true, -- Darker colors for diagnostic
    undercurl = true, -- Use undercurl for diagnostics
    background = true, -- Use background color for virtual text
  },
  -- The following table accepts values the same as the `gui` option for normal
  -- highlights. For example, `bold`, `italic`, `underline`, `none`.
  code_style = {
    comments = "italic",
    conditionals = "none",
    functions = "none",
    keywords = "none",
    headings = "bold", -- Markdown headings
    operators = "none",
    keyword_return = "none",
    strings = "none",
    variables = "none",
  },

  -----PLUGINS-----
  --
  -- The following options allow for more control over some plugin appearances.
  plugin = {
    lualine = {
      -- Bold lualine_a sections
      bold = true,
      -- Don't set section/component backgrounds. Recommended to not set
      -- section/component separators.
      plain = false,
    },
    cmp = { -- works for nvim.cmp and blink.nvim
      -- Don't highlight lsp-kind items. Only the current selection will be highlighted.
      plain = false,
      -- Reverse lsp-kind items' highlights in blink/cmp menu.
      reverse = false,
    },
  },

  -- CUSTOM HIGHLIGHTS --
  --
  -- Override default colors
  colors = {},
  -- Override highlight groups
  highlights = {},
})
-- Convenience function that simply calls `:colorscheme <theme>` with the theme
-- specified in your config.
require("black-metal").load()
```

## Customization

Example using custom colors and highlights:

```lua
require("black-metal").setup {
  colors = {
    orange = '#ff8800', -- define a new color
    keyword = '#817faf', -- redefine an existing color
  },
  highlights = {
    ...
    ["@keyword"] = { fg = "$keyword", fmt = 'bold' },
    ["@function"] = { bg = "$orange", fmt = 'underline,italic' },
    ...
  },
}
```

See `black-metal.palette` for color names.

## Cover references

- Bathory: Hammerheart, 1990
- Burzum: Filosofem, 1996
- Dark Funeral: The secrets of the black arts, 1996
- Darkthrone: Transilvanian Hunger, 1994
- Emperor: In the nightside eclipse, 1994
- Gorgoroth: Twilight of the Idols - In Conspiracy with Satan, 2003
- Immortal: At the heart of winter, 1999
- Impaled Nazarene: Tol Cormpt Norz Norz Norz..., 1993
- Khold: Phantom, 2002
- Marduk: Panzer Division Marduk, 1999
- Mayhem: The dawn of the black hearts, 1995
- Nile: Black seeds of vengeance, 2000
- Taake:  Hordalands doedskvad, 2005
- Venom: Welcome to hell, 1981

## Disclaimers

- I know Nile don't play black metal, but I don't want to name the repo 'Black Metal and Technical Death Metal' ;).
- Bands and album choices have been made completely on personal taste. If your fave band is missing, just ask and I'll try adding it.


