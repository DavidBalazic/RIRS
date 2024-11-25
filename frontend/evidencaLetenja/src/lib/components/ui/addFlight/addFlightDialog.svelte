<script lang="ts">
    import * as Dialog from "$lib/components/ui/dialog/index.js";
    import { Button } from "$lib/components/ui/button";
    import { Input } from "$lib/components/ui/input/index.js";
    import { Label } from "$lib/components/ui/label/index.js";
    import Datepicker from "@/components/ui/datepicker/datepicker.svelte";
    import { type DateValue, getLocalTimeZone } from "@internationalized/date";

    export let onSave: (data: {
        cas_vzleta: string;
        cas_pristanka: string;
        Pilot_idPilot: number;
    }) => void;

    let isDialogOpen = false;
    let cas_vzleta: DateValue | undefined = undefined;
    let cas_pristanka: DateValue | undefined = undefined;
    let Pilot_idPilot = 0;

    async function handleSave() {
        const formattedVzleta = cas_vzleta
            ? cas_vzleta.toDate(getLocalTimeZone()).toISOString()
            : "";
        const formattedPristanka = cas_pristanka
            ? cas_pristanka.toDate(getLocalTimeZone()).toISOString()
            : "";

        const flightData = {
            cas_vzleta: formattedVzleta,
            cas_pristanka: formattedPristanka,
            Pilot_idPilot,
        };

        onSave(flightData);
        isDialogOpen = false;
    }
</script>

<Dialog.Root bind:open={isDialogOpen}>
    <Dialog.Trigger
        class="mt-6 bg-blue-600 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
    >
        Dodaj
    </Dialog.Trigger>
    <Dialog.Content class="sm:max-w-[425px]">
        <Dialog.Header>
            <Dialog.Title>Nov polet</Dialog.Title>
            <Dialog.Description>
                Tukaj lahko dodate nov polet.
            </Dialog.Description>
        </Dialog.Header>
        <div class="grid gap-4 py-4">
            <div class="grid grid-cols-4 items-center gap-4">
                <Label for="cas_vzleta" class="text-right">Čas vzleta</Label>
                <Datepicker id="cas_vzleta" bind:value={cas_vzleta} />
            </div>
            <div class="grid grid-cols-4 items-center gap-4">
                <Label for="cas_pristanka" class="text-right"
                    >Čas pristanka</Label
                >
                <Datepicker id="cas_pristanka" bind:value={cas_pristanka} />
            </div>
            <div class="grid grid-cols-4 items-center gap-4">
                <Label for="id_pilota" class="text-right">ID Pilota</Label>
                <Input
                    id="id_pilota"
                    type="number"
                    bind:value={Pilot_idPilot}
                    class="col-span-3"
                />
            </div>
        </div>
        <Dialog.Footer>
            <Button on:click={handleSave}>Shrani</Button>
        </Dialog.Footer>
    </Dialog.Content>
</Dialog.Root>
