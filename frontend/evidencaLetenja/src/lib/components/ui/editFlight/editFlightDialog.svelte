<script lang="ts">
    import * as Dialog from "$lib/components/ui/dialog/index.js";
    import { Button } from "$lib/components/ui/button";
    import { Input } from "$lib/components/ui/input/index.js";
    import { Label } from "$lib/components/ui/label/index.js";
    import Datepicker from "@/components/ui/datepicker/datepicker.svelte";
    import { type DateValue } from "@internationalized/date";
    import { CalendarDateTime } from "@internationalized/date";

    export let polet: {
        idPolet: number;
        cas_vzleta: string;
        cas_pristanka: string;
        Pilot_idPilot: number;
    };

    export let onSave: (flightData: {
        idPolet: number;
        cas_vzleta: string;
        cas_pristanka: string;
        Pilot_idPilot: number;
    }) => void;

    let isDialogOpen = false;
    let cas_vzleta: DateValue = parseDateTime(polet.cas_vzleta);
    let cas_pristanka: DateValue = parseDateTime(polet.cas_pristanka);
    let Pilot_idPilot = polet.Pilot_idPilot;

    function handleSave() {
        const updatedFlightData = {
            idPolet: polet.idPolet,
            cas_vzleta: formatDateTime(cas_vzleta),
            cas_pristanka: formatDateTime(cas_pristanka),
            Pilot_idPilot: Pilot_idPilot,
        };

        onSave(updatedFlightData);

        isDialogOpen = false;
    }

    function formatDateTime(dateTime: DateValue): string {
        if (!dateTime) return "";
        const date = new Date(dateTime.toString());
        const day = String(date.getDate()).padStart(2, "0");
        const month = String(date.getMonth() + 1).padStart(2, "0");
        const year = date.getFullYear();
        const hours = String(date.getHours()).padStart(2, "0");
        const minutes = String(date.getMinutes()).padStart(2, "0");
        return `${day}/${month}/${year} ${hours}:${minutes}`;
    }

    function parseDateTime(dateTimeStr: string): DateValue {
        if (!dateTimeStr) return new CalendarDateTime(1970, 1, 1, 0, 0);

        const [datePart, timePart] = dateTimeStr.split(" ");
        const [day, month, year] = datePart.split("/").map(Number);
        const [hours, minutes] = timePart.split(":").map(Number);

        return new CalendarDateTime(year, month, day, hours, minutes);
    }
</script>

<Dialog.Root bind:open={isDialogOpen}>
    <Dialog.Trigger
        class="mt-6 bg-blue-600 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
    >
        Uredi
    </Dialog.Trigger>
    <Dialog.Content class="sm:max-w-[425px]">
        <Dialog.Header>
            <Dialog.Title>Uredi polet</Dialog.Title>
            <Dialog.Description>
                Tukaj lahko urejate podatke o vašem letu.
            </Dialog.Description>
        </Dialog.Header>
        <div class="grid gap-4 py-4">
            <div class="grid grid-cols-4 items-center gap-4">
                <Label for="cas_vzleta" class="text-right">Čas vzleta</Label>
                <Datepicker bind:value={cas_vzleta} />
            </div>
            <div class="grid grid-cols-4 items-center gap-4">
                <Label for="cas_pristanka" class="text-right"
                    >Čas pristanka</Label
                >
                <Datepicker bind:value={cas_pristanka} />
            </div>
            <div class="grid grid-cols-4 items-center gap-4">
                <Label for="id_pilota" class="text-right">Pilot ID</Label>
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
