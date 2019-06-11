#### tmux是什么？

>Terminal Multiplexer，它是一个多终端进程管理器.
>主要用到的功能：配合iTerm2多终端界面分屏显示，后台运行终端进程.
>
>它的主要功能也是用它主要原因，当然它的功能远非这些
>
>另外：iTerm2的最新版已经集成了tumx，建议单独安装tmux来配合iTerm2使用。


#### Tmux 的快捷键前缀（Prefix）
>为了使自身的快捷键和其他软件的快捷键互不干扰，Tmux 提供了一个快捷键前缀。当想要使用快捷键时，需要先按下快捷键前缀，然后再按下快捷键。Tmux 所使用的快捷键前缀默认是组合键 Ctrl-b（同时按下 Ctrl 键和 b 键）。例如，假如你想通过快捷键列出当前 Tmux 中的会话（对应的快捷键是 s），那么你只需要做以下几步：
>
>     按下组合键 Ctrl-b (Tmux 快捷键前缀)
>     放开组合键 Ctrl-b
>     按下 s 键

#### macOS 上安装Tmux
>brew install tmux


#### 设置tmux
>建议将 Tmux 的快捷键前缀变为 Ctrl - a。按下 Ctrl - a 就将会比按下 Ctrl - b更容易、更便捷。
>
>若要将快捷键前缀变更为 Ctrl-a ，请将以下配置加入到 Tmux 的配置文件 ~/.tmux.conf 中: 
>
>     unbind C-b 
>     set -g prefix C-a
>
>每当开启一个新的会话时，Tmux 都会先读取 ~/.tmux.conf 这个文件。该文件中存放的就是对 Tmux 的配置。

>小提示：如果你希望新的配置项能够立即生效，那么你可以将下面这一行配置加入到文件~/.tmux.conf 中。
>
>     # bind a reload key
>     bind R source-file ~/.tmux.conf ; display-message "Config reloaded.."
>这样配置了之后，每当向 ~/.tmux.conf 文件中添加了新的配置，只需要按下 Ctrl-b r就可以重新加载配置并使新的配置生效，从而免去了开启一个新的会话。
