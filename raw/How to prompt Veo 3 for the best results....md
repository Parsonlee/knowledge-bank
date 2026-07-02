---
id: "7350507002675594556"
cubox_url: https://cubox.pro/web/card/7350507002675594556
url: https://replicate.com/blog/using-and-prompting-veo-3
tags:
  - AIGC
---
# How to prompt Veo 3 for the best results – Replicate blog

Learn expert prompting techniques to create stunning videos with Google's Veo 3.

[Read in Cubox](https://cubox.pro/web/card/7350507002675594556)  
[Read Original](https://replicate.com/blog/using-and-prompting-veo-3)  

---


---

## 📖 正文全文

# How to prompt Veo 3 for the best results

[replicate.com](https://replicate.com/blog/using-and-prompting-veo-3)

Ready to give it a spin?
[Try Veo 3](https://replicate.com/google/veo-3)

[Google's Veo 3](https://replicate.com/google/veo-3) generates videos with audio from text prompts. The audio can be dialogue, voice-overs, sound effects and music.

Let our resident AI podcaster introduce us:
Prompt: A podcast show, a woman in a grey sweater and dark brown tousled hair in an updo, she looks directly at the camera, with strands framing her face. She talks into a mic saying: This is Replicate's guide to prompting Veo 3...

## Write what happens

First the basics. A well-crafted prompt is the key to generating good videos. The more you can specify in your prompt, in plain language, the easier it is for Veo 3 to understand and generate the video you want.

Try to include these visual elements in your prompt:

1. Subject: Who or what is in the scene --- a person, animal, object, or landscape.
2. Context: Where is the subject? Indoors? A city street? A forest?
3. Action: Is your subject walking, jumping, turning their head?
4. Style: The visual aesthetic you're aiming for (cinematic, animated, stop-motion, etc).
5. Camera motion: Describe how the camera moves: aerial shot, eye-level, top-down, or low-angle.
6. Composition: How the shot is framed: wide shot, close-up, etc.
7. Ambiance: Mood and lighting. You can say things like "warm tones," "blue light," or "nighttime."

You also need to include audio elements, which we'll cover in more detail below.

Here's an example of a basic prompt versus a detailed one:
> A man answers a rotary phone

Versus:
> A shaky dolly zoom goes from a far away blur to a close-up cinematic shot of a desperate man in a weathered green trench coat as he picks up a rotary phone mounted on a gritty brick wall, bathed in the eerie glow of a green neon sign. The zoom reveals the tension and the desperation etched on his face as he struggles to talk on the phone. The shallow depth of field focuses on his furrowed brow and the black rotary phone, blurring the background into a sea of neon colors and indistinct shadows, creating a sense of urgency and isolation.

The second prompt contains structural elements to nudge Veo 3 towards the scene we are trying to create.

Your browser does not support the video tag.
Basic prompt

Your browser does not support the video tag.
Detailed prompt

### Change your prompt each time

If you're familiar with prompting models like Midjourney or [Flux](https://replicate.com/black-forest-labs/flux-1.1-pro), you'll know that with those models you'll get a decent level of variation if you run the same prompt a few times (ie using different seeds).

Veo 3 is different. For the same prompt, even one that's fairly simple, Veo 3 will output very similar results. You might get the same looking person in the same clothes, in a similar sort of place. This is excellent if you've had an output that has a slight error, like a coherency or audio glitch -- you can run a different seed and get what you want. But if you're in discovery mode, when you want to see a range of what's possible, then running the same prompt multiple times is a waste of your money.

In the example below we ran the prompt "a woman laughs" twice, with different seeds. Note how she looks the same, she's wearing the same clothes, she laughs in the same way, the room is the same, she's even wearing the same earrings. It's unusual for a model to be this consistent.

<br />

[First video](https://replicate.com/p/np8n7zm765rma0cq8tjs9pfnj8) [Second video](https://replicate.com/p/z4zf8gmea9rma0cq8tjrddzk34)

<br />

If you're not sure what you want yet, start with a few broadly different prompts. If you know elements of what you want, then be specific about those.

In this video the obvious things we could do are begin to play with descriptions for:

* how the woman looks (hair color, hair style, skin color)
* what she's wearing
* where she is
* how she is laughing
* why she is laughing

Here are a couple of examples:

<br />

a woman laughs long and loudly, she's in an office meeting and she's embarrassed afterwards a woman laughs quietly, she's at home watching a tv show

<br />

## Character consistency

Typically character consistency is hard when you're using a video model without a starting frame or scene ingredients. These features are coming to Veo 3 soon.

In the meantime, because similar prompts yield similar characters, if you keep a character's detailed prompt description consistent across generations, you'll often get someone who looks the same. This means you can keep a list of character descriptions and repeat them verbatim across different prompts:
> John, a man in his 40s with short brown hair, wearing a blue jacket and glasses, looking thoughtful

The more unique and specific these descriptions, the better Veo 3 maintains visual continuity between separately generated scenes. Create character reference sheets with exact wording to ensure consistency.

<br />

John, a man in his 40s with short brown hair, wearing a blue jacket and glasses, looking thoughtful, he says: Hello, I am also John, and I look kind of the same as that guy over there (no subtitles!). He is in a bright light room. John, a man in his 40s with short brown hair, wearing a blue jacket and glasses, looking thoughtful, he says: Hello, my name is John, I am a character invented for this blog post (no subtitles!)

<br />

## Prompting audio

As Veo 3 generates audio with each video, you also need to prompt for the audio you want to hear. Consider these elements:

1. What people are saying (dialogue)
2. The ambient noise of the scene (the sounds of a busy street, a busy office, a busy cafe, etc)
3. Sound effects or noises from outside the scene (like a phone ringing)
4. Any music the scene might need (a tense cinematic score, a cheerful pop song, etc).

### Prompting dialogue and avoiding subtitles

The characters you can create with Veo 3 are fascinating. They talk, tell jokes, gesticulate, sometimes they can act. But if you want them to talk, you need to prompt for that.

You can prompt dialogue in two different ways:

1. Explicitly: "A guy says: My name is Ben"
2. Implicitly: "A guy tells us his name"

Both of these will lead to a video of a guy talking, the first will use the exact words you asked for, the second will let the model decide how to say it, in this case the model will decide on a name for you.

#### Writing your own dialogue

If you're being explicit about what's being said, try to keep your dialogue short. It should be something that can be said in just about 8 seconds.

If you try to pack too much in, then you can end up with a character that's speaking way too fast. If you ask them to say too little, you can get either awkward silences or a character saying nonsensical AI gibberish (like the second example below). Without clear guidance the model won't be able to make up all the words it needs to.

<br />

John, a man in his 40s with short brown hair, wearing a blue jacket and glasses, looking thoughtful, he says: You have given me a really long prompt, and I have to speak very quickly and unnaturally to try and fit all these words into just 8 seconds, I'm going to be out of breath at the end of this, phew. Too short (and with AI gibberish): John, a man in his 40s with short brown hair, wearing a blue jacket and glasses, looking thoughtful, he says: Hello, I'm John.

<br />

#### Letting Veo 3 script the dialogue

If you aren't good at writing dialogue, implicit dialogue prompts will help. And you can always transcribe the outputs you liked for use in later prompts.

Here we ask Veo 3 to create a video of a standup comic telling a joke, first we let Veo 3 decide on the joke. Second video we get Veo 3 to try and deliver the joke we put in the prompt.

<br />

a standup comic tells an awkward joke at a music festival, sounds of distant bands, noisy crowd, ambient background of a busy festival field (no studio audience) a standup comic tells an awkward joke at a music festival: You know what's great about music festivals? Watching 20,000 people pretend they knew this band before today while filming vertical videos they'll never watch.

<br />

As you can see, given the right prompt and all the appropriate context, Veo 3 can fill in the dialogue for you.

Some prompts you could try to see how versatile Veo 3 is with dialogue:

* a standup comic tells a joke
* two people discuss a movie
* a man is having an argument over the phone
* a woman tells us her life story

#### Getting pronunciation right

Sometimes you'll find that the model is pronouncing words incorrectly. The easiest way to handle this is to spell the words phonetically. In the opening example, our podcaster says:
> Read on to get fofr and Shridar's guidance on making videos

But to get the correct pronunciation for our names, we had to change the prompt to:
> Read on to get foh-fur's and Shreedar's guidance on making videos

#### Who says what

When you prompt a conversation between multiple characters you will sometimes find that Veo 3 mixes up who says what. This is common when the characters have similar descriptions, and it's ambiguous to Veo 3 which character is which.

Try to be specific in your prompt about who is speaking:
> The woman wearing pink says: But I'm the one who's wearing pink
> The man with the glasses replies: No, I'm the one with the glasses

### Avoiding subtitles in outputs

Veo 3 must have been trained on plenty of videos with baked-in subtitles, because it's very common to see poorly spelled and incorrect subtitles in the outputs. They often ruin a generation, but there are a couple of easy ways to avoid them:

* put the speech you want to hear after a colon, like: "A guy says: My name is Ben" rather than in quotes, like: "A guy says: 'My name is Ben"
* put "(no subtitles)" in the prompt, negatives work well in Veo 3 prompts
* if all else fails, keep saying No subtitles. No subtitles! Multiple times.

### The wrong background audio (or the case of the unwanted live studio audience)

If you don't define the background audio you want to hear in your video, then Veo 3 needs to work it out, often that's ok, but sometimes it gets it wrong. A live studio audience is a common hallucination. Sometimes it's what you want, like a fake sitcom. But usually the extra laughter doesn't fit the scene. Veo 3 even did this when making the examples above, here's an example of an out of place studio audience ruining a generation:
Example of unwanted studio audience laughter in the background.  
Prompt: "a standup comic tells an awkward joke at a music festival"

The easiest way to avoid this is to prompt the audio you expect to hear explicitly. In this case we fixed the generation by adding "sounds of distant bands, noisy crowd, ambient background of a busy festival field" to get the right sort of feeling in the output.

## Prompting music

Just like the rest of the video, if you want music in your scene you need to include it in your prompt.

Again, you can be explicit and describe the genre, style and mood of the music you want to hear. Or you can be more vague and let Veo 3 decide.

## Styles

Out of the box Veo 3 will typically generate something that looks like a well-produced live action video, think smooth professional demo, a commercial or a music video.

If you want to steer it away from this you need to include a style with your prompt. Here are some examples of styles Veo 3 knows how to generate, the prompt is:
> In the style of \[style name\]: A bearded man in a flannel shirt and weathered jeans sits cross-legged beside a flickering campfire, its amber light casting soft, dancing shadows across the pine-needle-strewn ground of a quiet forest clearing. Across from him, just beyond the edge of the firelight, stands a massive grizzly bear, calm and still, its fur catching the warm glow, eyes reflecting the flames with eerie intelligence. The two shake hands, like they're old friends.

You'll notice that not only does the look of the video change, but also the way the characters move and interact too.

In each of these, the audio remains very similar, we haven't prompted the audio differently, and it hasn't changed much between the different styles.

Your browser does not support the video tag.
Original video

Your browser does not support the video tag.
LEGO

Your browser does not support the video tag.
Claymation

Your browser does not support the video tag.
South Park

Your browser does not support the video tag.
Pixar animation

Your browser does not support the video tag.
8-bit retro

Your browser does not support the video tag.
Graphic novel

Your browser does not support the video tag.
Origami

Your browser does not support the video tag.
Simpsons

Your browser does not support the video tag.
Blueprint

Your browser does not support the video tag.
Anime

Your browser does not support the video tag.
Marble

## Camera motion

As you might expect, just like other video models, Veo 3 responds well to common camera movement prompts. Using terms like these, you can control the action in your video:

* eye level
* high angle
* worms eye
* dolly shot
* zoom shot
* pan shot
* tracking shot

Your browser does not support the video tag.
Zoom in

Your browser does not support the video tag.
Zoom out

Your browser does not support the video tag.
Left to right pan

Your browser does not support the video tag.
Dolly shot

## Selfie-style videos

Veo 3 is surprisingly good at making selfie videos that actually look real. We've found that certain phrases seem to unlock this behavior consistently.

Starting with "A selfie video of..." works much better than just describing a person with a camera.

Making the arm visible is key for authenticity. The gorilla example shows this well with "holds the camera at arm's length. His long, powerful arm is clearly visible in the frame." That's what makes it look like an actual selfie rather than a close-up shot.

Natural eye movement also helps a lot. The Tokyo example shows this with "occasionally looking into the camera before turning to point at interesting stalls." That kind of natural glancing behavior works better than staring directly at the camera.

Here are two examples that show how this works:
> A selfie video of a travel blogger exploring a bustling Tokyo street market. She's wearing a vintage denim jacket and has excitement in her eyes. The afternoon sun creates beautiful shadows between the vendor stalls. She's sampling different street foods while talking, occasionally looking into the camera before turning to point at interesting stalls. The image is slightly grainy, looks very film-like. She speaks in a British accent and says: "Okay, you have to try this place when you visit Tokyo. The takoyaki here is absolutely incredible, and the vendor just told me it's been in his family for three generations." She ends with a thumbs up.
> A handheld selfie-style shot, from the point-of-view of a gorilla in a lush jungle. A large silverback gorilla holds the camera at arm's length. His long, powerful arm is clearly visible in the frame, and his face is perfectly framed. The gorilla says: "I'm just testing out this actually works and I'm going to post it on TikTok later, Essentially it felt cute might delete it later" (lips moving like he's saying it)

<br />

Tokyo travel blogger Gorilla selfie

<br />

One more thing the Tokyo example shows: adding "The image is slightly grainy, looks very film-like" seems to push the output away from that too-clean AI look. It ends up feeling more like something that was actually shot on a phone.

## How to make vertical videos with Veo 3

At the moment Veo 3 doesn't natively support vertical videos, only 16:9 horizontal are possible. You can however take a landscape video and outpaint it using a model like [Luma's Reframe Video](https://replicate.com/luma/reframe-video).

Reframe video lets you pass in any video (up to 30 seconds long), and outpaints it as a new video at the specified aspect ratio. All outputs will be 720p.
A Veo 3 video that was reframed as a 9:16 vertical video

Native support for vertical videos in Veo 3 is coming soon.

## Physics

Veo 3 excels at simulating realistic physics, maintaining proper motion and interactions while applying different styles. The model preserves the natural movement of objects, ensuring that physics-based animations like falling, bouncing, and fluid motion remain physically accurate even when transformed into different artistic styles.

Your browser does not support the video tag.
LEGO

Your browser does not support the video tag.
Origami

Your browser does not support the video tag.
Chrome

Your browser does not support the video tag.
Paint

## Upscaling to 4k and 60fps

By default, Veo 3 outputs 1280p x 720p video. We recommend using [Topaz Lab's Video Upscaler](https://replicate.com/topazlabs/video-upscale) to bring your videos up to 4k resolution and 60 frames-per-second.

## Final remarks

The difference between a bland video and a great one comes down to your prompt. With Veo 3, you're not just describing what happens, you're directing a scene. High quality videos will layer in subject, setting, action, camera work, audio and mood. Think like a filmmaker and [Veo 3](https://replicate.com/google/veo-3) will follow your lead.

One final prompt:
> A podcast show, a woman in a grey sweater and dark brown tousled hair in an updo, with strands framing her face. She is in a room with pink and gold uplighting. No subtitles. She is giving an outro and looks directly at the camera as she talks into a mic saying (no subtitles!): So that's the end of our guide, we hope you found it useful. Feel free to [try Veo 3 on Replicate](https://replicate.com/google/veo-3), and don't forget to [follow us on X](https://x.com/replicate).

[Read in Cubox](https://cubox.pro/web/card/7350507002675594556)
