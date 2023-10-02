# Why is lazy evaluation useful?

<div><div>
<p>I find lazy evaluation useful for a number of things.</p>
<p><strong>First</strong>, all existing lazy languages are pure, because it is very hard to reason about side effects in a lazy language.</p>
<p>Pure languages let you reason about function definitions using equational reasoning.</p>
<pre><code>foo x = x + 3
</code></pre>
<p>Unfortunately in a non-lazy setting, more statements fail to return than in a lazy setting, so this is less useful in languages like ML. But in a lazy language you can safely reason about equality.</p>
<p><strong>Secondly</strong>, a lot of stuff like the 'value restriction' in ML aren't needed in lazy languages like Haskell. This leads to a great decluttering of syntax. ML like languages need to use keywords like var or fun. In Haskell these things collapse down to one notion.</p>
<p><strong>Third</strong>, laziness lets you write very functional code that can be understood in pieces. In Haskell it is common to write a function body like:</p>
<pre><code>foo x y = if condition1
 then some (complicated set of combinators) (involving bigscaryexpression)
 else if condition2
 then bigscaryexpression
 else Nothing
 where some x y = ...
 bigscaryexpression = ...
 condition1 = ...
 condition2 = ...
</code></pre>
<p>This lets you work 'top down' though the understanding of the body of a function. ML-like languages force you to use a <code>let</code> that is evaluated strictly. Consequently, you don't dare 'lift' the let clause out to the main body of the function, because if it expensive (or has side effects) you don't want it always to be evaluated. Haskell can 'push off' the details to the where clause explicitly because it knows that the contents of that clause will only be evaluated as needed.</p>
<p>In practice, we tend to use guards and collapse that further to:</p>
<pre><code>foo x y 
 | condition1 = some (complicated set of combinators) (involving bigscaryexpression)
 | condition2 = bigscaryexpression
 | otherwise = Nothing
 where some x y = ...
 bigscaryexpression = ...
 condition1 = ...
 condition2 = ...
</code></pre>
<p><strong>Fourth</strong>, laziness sometimes offers much more elegant expression of certain algorithms. A lazy 'quick sort' in Haskell is a one-liner and has the benefit that if you only look at the first few items, you only pay costs proportional to the cost of selecting just those items. Nothing prevents you from doing this strictly, but you'd likely have to recode the algorithm each time to achieve the same asymptotic performance.</p>
<p><strong>Fifth</strong>, laziness allows you to define new control structures in the language. You can't write a new 'if .. then .. else ..' like construct in a strict language. If you try to define a function like:</p>
<pre><code>if' True x y = x
if' False x y = y
</code></pre>
<p>in a strict language then both branches would be evaluated regardless of the condition value. It gets worse when you consider loops. All strict solutions require the language to provide you with some sort of quotation or explicit lambda construction.</p>
<p><strong>Finally</strong>, in that same vein, some of the best mechanisms for dealing with side-effects in the type system, such as monads, really can only be expressed effectively in a lazy setting. This can be witnessed by comparing the complexity of F#'s Workflows to Haskell Monads. (You can define a monad in a strict language, but unfortunately you'll often fail a monad law or two due to lack of laziness and Workflows by comparison pick up a ton of strict baggage.)</p>
 </div>

