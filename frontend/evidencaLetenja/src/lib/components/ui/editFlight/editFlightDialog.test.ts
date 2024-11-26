import { render, fireEvent, screen } from "@testing-library/svelte";
import EditFlightDialog from "./EditFlightDialog.svelte";

test("opens dialog when 'Uredi' button is clicked", async () => {
  render(EditFlightDialog, {
    props: {
      polet: {
        idPolet: 1,
        cas_vzleta: "25/11/2024 10:00",
        cas_pristanka: "25/11/2024 12:00",
        Pilot_idPilot: 42,
      },
      onSave: vi.fn(),
    },
  });

  const triggerButton = screen.getByRole("button", { name: /uredi/i });
  await fireEvent.click(triggerButton);

  const dialogTitle = await screen.findByText(/uredi polet/i);
  expect(dialogTitle).toBeInTheDocument();
});

test("dialog fields are pre-filled with provided polet data", async () => {
    render(EditFlightDialog, {
      props: {
        polet: {
          idPolet: 1,
          cas_vzleta: "25/11/2024 10:00",
          cas_pristanka: "25/11/2024 12:00",
          Pilot_idPilot: 42,
        },
        onSave: vi.fn(),
      },
    });
  
    const triggerButton = screen.getByRole("button", { name: /uredi/i });
    await fireEvent.click(triggerButton);
  
    const pilotIdInput = screen.getByLabelText(/pilot id/i);
    expect(pilotIdInput).toHaveValue(42);
  });
  
  test("calls onSave with updated data when save is clicked", async () => {
    const onSaveMock = vi.fn();
    render(EditFlightDialog, {
      props: {
        polet: {
          idPolet: 1,
          cas_vzleta: "25/11/2024 10:00",
          cas_pristanka: "25/11/2024 12:00",
          Pilot_idPilot: 42,
        },
        onSave: onSaveMock,
      },
    });
  
    const triggerButton = screen.getByRole("button", { name: /uredi/i });
    await fireEvent.click(triggerButton);
  
    const pilotIdInput = screen.getByLabelText(/pilot id/i);
    await fireEvent.input(pilotIdInput, { target: { value: "45" } });
  
    const saveButton = screen.getByRole("button", { name: /shrani/i });
    await fireEvent.click(saveButton);
  
    expect(onSaveMock).toHaveBeenCalledWith({
      idPolet: 1,
      cas_vzleta: "25/11/2024 10:00",
      cas_pristanka: "25/11/2024 12:00",
      Pilot_idPilot: 45,
    });
  });

  test("dialog is closed initially", () => {
    render(EditFlightDialog, {
      props: {
        polet: {
          idPolet: 1,
          cas_vzleta: "25/11/2024 10:00",
          cas_pristanka: "25/11/2024 12:00",
          Pilot_idPilot: 42,
        },
        onSave: vi.fn(),
      },
    });
  
    expect(screen.queryByText(/uredi polet/i)).not.toBeInTheDocument();
  });
