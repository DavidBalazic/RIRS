<script lang="ts">
    import * as Carousel from "$lib/components/ui/carousel/index.js";
    import Button from "@/components/ui/button/button.svelte";
    import { onMount } from "svelte";
    import * as Table from "$lib/components/ui/table/index.js";
    import { Cell } from "@/components/ui/calendar";
    import AddPlaneDialog from "$lib/components/ui/addPlane/addPlaneDialog.svelte";
    import { env } from '$env/dynamic/public';
    
    type Plane = {
      idLetalo: number;
      ime_letala: string;
      tip: string;
      registrska_st: string;
      Polet_idPolet: number;
    };
  
    let planes: Plane[] = [];

    const backendUrl = env.PUBLIC_BACKEND_URL
  
    async function getPlanes() {
      try {
        const response = await fetch(`${backendUrl}/pridobiLetala/`);
        if (response.ok) {
            planes = await response.json();
        } else {
          console.error("Failed to fetch planes data");
        }
      } catch (error) {
        console.error("Error fetching planes data:", error);
      }
    }

    async function handlePlaneSave(planeData: {
      ime_letala: string;
      tip: string;
      registrska_st: string;
      Polet_idPolet: number;
    }) {
        try {
            const response = await fetch(`${backendUrl}/dodajLetalo/`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(planeData),
            });

            if (!response.ok) {
                throw new Error("Failed to save plane data");
            }

            const result = await response.json();
            console.log("Plane saved successfully:", result);
            refreshPage();
        } catch (error) {
            console.error("Error saving plane:", error);
        }
    }

  

    async function deletePlane(id: number) {
        const response = await fetch(`${backendUrl}/letalo/${id}`, {
            method: "DELETE",
        });
        if (response.ok) {
            planes = planes.filter((plane) => plane.idLetalo !== id);
            console.log("Izbrisano letalo:", id);
        } else {
            console.error("Letalo ni bilo uspešno izbrisano:", response.statusText);
        }
    }

    onMount(() => {
        console.log(planes)
      getPlanes();
    });

    function refreshPage() {
      getPlanes();
    }

  </script>
  
  <main class=" flex flex-col gap-6 max-w-7xl mx-auto px-4 py-8">
    <section>
      <h1 class="scroll-m-20 text-4xl font-extrabold tracking-tight lg:text-5xl mb-8 text-center text-gray-800">
        Letala
      </h1>
    </section>

    <section>
      <AddPlaneDialog onSave={handlePlaneSave} />
    </section>
  
    <section>
      <Carousel.Root>
        <Carousel.Content class="flex gap-4">
          {#each planes as plane}
            <Carousel.Item class="carousel-item">
              <div class="plane-card w-full max-w-7xl mx-auto p-6 rounded-lg border-solid border-2 border-indigo-500 shadow-md bg-white transition-transform duration-300 hover:scale-105 hover:shadow-lg">
                <h2 class="text-2xl font-semibold text-gray-800 mb-2">{plane.ime_letala}</h2>
                <p class="text-gray-600"><strong>Tip:</strong> {plane.tip}</p>
                <p class="text-gray-600"><strong>Registracijska številka:</strong> {plane.registrska_st}</p>
                <p class="text-gray-600"><strong>Letalo ID:</strong> {plane.idLetalo}</p>
                <p class="text-gray-600"><strong>Polet ID:</strong> {plane.Polet_idPolet}</p>
                <Button class="bg-red-500 text-white" on:click={() => deletePlane(plane.idLetalo)}>Izbrisi letalo</Button>
              </div>
            </Carousel.Item>
          {/each}
        </Carousel.Content>
        <Carousel.Previous class="carousel-control" />
        <Carousel.Next class="carousel-control" />
      </Carousel.Root>
    </section>

    <section>
      <Table.Root>
          <Table.Header>
              <Table.Row class="table-row">
                  <Table.Head>ID</Table.Head>
                  <Table.Head>Ime letala</Table.Head>
                  <Table.Head>Registrska številka</Table.Head>
                  <Table.Head>Tip letala</Table.Head>
                  <Table.Head>Izbriši</Table.Head>
              </Table.Row>
          </Table.Header>
          <Table.Body>
              {#each planes as plane}
                  <Table.Row>
                      <Table.Cell>{plane.idLetalo}</Table.Cell>
                      <Table.Cell>{plane.ime_letala}</Table.Cell>
                      <Table.Cell>{plane.registrska_st}</Table.Cell>
                      <Table.Cell>{plane.tip}</Table.Cell>
                      <Table.Cell><Button class="bg-red-500 text-white" on:click={() => deletePlane(plane.idLetalo)}>Izbrisi letalo</Button></Table.Cell>
                  </Table.Row>
              {/each}
          </Table.Body>
      </Table.Root>
  </section>
  </main>
  
  <style>
    .carousel-item {
      display: flex;
      justify-content: center;
      width: 100%;
      padding: 1rem;
    }
  
    .plane-card {
      width: 100%;
      background: white;
      border-radius: 0.75rem;
      padding: 1.5rem;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
      transition: transform 0.3s, box-shadow 0.3s;
    }
  
    .plane-card:hover {
      transform: scale(1.02);
      box-shadow: 0 8px 12px rgba(0, 0, 0, 0.15);
    }
  
    .plane-card h2 {
      color: #2d3748;
    }
  
    .plane-card p {
      color: #4a5568;
      margin-bottom: 0.5rem;
    }
  
    .carousel-control {
      font-size: 1.5rem;
      color: #4a5568;
      background: transparent;
      border: none;
      cursor: pointer;
      transition: color 0.3s;
    }
  
    .carousel-control:hover {
      color: #2d3748;
    }
  </style>
  
  
  
  