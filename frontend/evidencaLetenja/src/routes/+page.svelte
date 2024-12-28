<script>
    import { Button } from "$lib/components/ui/button";
</script>

<main>
    <section class="hero">
        <h1
            class="scroll-m-20 text-4xl font-extrabold tracking-tight lg:text-5xl"
        >
            Dobrodošli v Evidenco letenja
        </h1>
        <h3 class="scroll-m-20 mt-6 text-2xl font-semibold tracking-tight">
            Vaša rešitev na enem mestu za enostavno sledenje in upravljanje
            letov.
        </h3>
        <a href="/mojiLeti">
            <Button class="mt-6 bg-blue-600 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
                Iskanje letov
            </Button>
        </a>
    </section>
</main>

<style>
    .hero {
        background: url("https://example.com/your-background-image.jpg")
            center/cover no-repeat; /* Add your image URL */
        height: 60vh;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        color: black;
    }
</style>
