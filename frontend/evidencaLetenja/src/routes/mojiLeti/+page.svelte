<script lang="ts">
    import * as Table from "$lib/components/ui/table/index.js";
    import { Button } from "$lib/components/ui/button";
    import AddFlightDialog from "$lib/components/ui/addFlight/addFlightDialog.svelte";
    import EditFlightDialog from "$lib/components/ui/editFlight/editFlightDialog.svelte";
    import { onMount } from "svelte";

    interface Polet {
        idPolet: number;
        cas_vzleta: string;
        cas_pristanka: string;
        Pilot_idPilot: number;
    }

    let poleti: Polet[] = [];

    const backendUrl = import.meta.env.VITE_BACKEND_URL

    async function fetchFlights() {
        const response = await fetch(`${backendUrl}/pridobiPrihodnjeLete/`);
        if (!response.ok) {
            console.error("Failed to fetch flights:", response.statusText);
            return;
        }
        const data = await response.json();
        poleti = data;
    }

    async function deleteFlight(id: number) {
        const response = await fetch(`${backendUrl}/polet/${id}`, {
            method: "DELETE",
        });
        if (response.ok) {
            poleti = poleti.filter((polet) => polet.idPolet !== id);
            console.log("Flight deleted:", id);
        } else {
            console.error("Failed to delete flight:", response.statusText);
        }
    }

    async function handleFlightSave(flightData: {
        cas_vzleta: string;
        cas_pristanka: string;
        Pilot_idPilot: number;
    }) {
        const formatDateTime = (dateTime: string): string => {
            const date = new Date(dateTime);
            const day = String(date.getDate()).padStart(2, "0");
            const month = String(date.getMonth() + 1).padStart(2, "0");
            const year = date.getFullYear();
            const hours = String(date.getHours()).padStart(2, "0");
            const minutes = String(date.getMinutes()).padStart(2, "0");
            return `${day}/${month}/${year} ${hours}:${minutes}`;
        };

        const formattedFlightData = {
            ...flightData,
            cas_vzleta: formatDateTime(flightData.cas_vzleta),
            cas_pristanka: formatDateTime(flightData.cas_pristanka),
            pilot_idPilot: flightData.Pilot_idPilot,
        };

        try {
            const response = await fetch("${backendUrl}/dodajPolet/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(formattedFlightData),
            });

            if (!response.ok) {
                throw new Error("Failed to save flight data");
            }

            const result = await response.json();
            console.log("Flight saved successfully:", result);
            refreshPage();
        } catch (error) {
            console.error("Error saving flight:", error);
        }
    }

    async function handleEditSave(updatedFlightData: Polet) {
        try {
            console.log("updatedFlightData", updatedFlightData.Pilot_idPilot);
            const response = await fetch(
                `${backendUrl}/poleti/${updatedFlightData.idPolet}`,
                {
                    method: "PUT",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify(updatedFlightData),
                },
            );

            if (!response.ok) {
                throw new Error("Failed to update flight data");
            }

            console.log("Flight updated successfully:", updatedFlightData);
            refreshPage();
        } catch (error) {
            console.error("Error updating flight:", error);
        }
    }

    function parseCustomDate(dateString: string) {
        const [day, month, year, time] = dateString.split(/[/\s:]/);
        return new Date(`${year}-${month}-${day}T${time}:00`);
    }

    function refreshPage() {
        fetchFlights();
    }

    onMount(() => {
        fetchFlights();
    });
</script>

<main class="max-w-7xl mx-auto px-4 py-8">
    <section>
        <h1
            class="scroll-m-20 text-4xl font-extrabold tracking-tight lg:text-5xl mb-6"
        >
            Moji leti
        </h1>
    </section>
    <section>
        <AddFlightDialog onSave={handleFlightSave} />
    </section>
    <section>
        <Table.Root>
            <Table.Header>
                <Table.Row class="table-row">
                    <Table.Head class="w-[100px]">ID</Table.Head>
                    <Table.Head class="text-right">Čas vzleta</Table.Head>
                    <Table.Head class="text-right">Čas pristanka</Table.Head>
                    <Table.Head class="text-right">Pilot ID</Table.Head>
                </Table.Row>
            </Table.Header>
            <Table.Body>
                {#each poleti as polet}
                    <Table.Row>
                        <Table.Cell>{polet.idPolet}</Table.Cell>
                        <Table.Cell class="text-right">
                            {polet.cas_vzleta
                                ? parseCustomDate(
                                      polet.cas_vzleta,
                                  ).toLocaleString("sl-SI", {
                                      dateStyle: "short",
                                      timeStyle: "short",
                                  })
                                : "Invalid Date"}
                        </Table.Cell>
                        <Table.Cell class="text-right">
                            {polet.cas_pristanka
                                ? parseCustomDate(
                                      polet.cas_pristanka,
                                  ).toLocaleString("sl-SI", {
                                      dateStyle: "short",
                                      timeStyle: "short",
                                  })
                                : "Invalid Date"}
                        </Table.Cell>
                        <Table.Cell class="text-right"
                            >{polet.Pilot_idPilot}</Table.Cell
                        >
                        <Table.Cell class="text-right">
                            <EditFlightDialog {polet} onSave={handleEditSave}
                            ></EditFlightDialog>
                            <Button
                                class="bg-red-500 text-white"
                                on:click={() => deleteFlight(polet.idPolet)}
                            >
                                Delete
                            </Button>
                        </Table.Cell>
                    </Table.Row>
                {/each}
            </Table.Body>
        </Table.Root>
    </section>
</main>
