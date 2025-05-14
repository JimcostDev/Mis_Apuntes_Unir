package main

import "fmt"

// Interfaz Observer
type Observer interface {
	Update(news string)
}

// Interfaz Subject
type Subject interface {
	Attach(observer Observer)
	Detach(observer Observer)
	Notify(news string)
}

// Implementación concreta de Subject
type NewsPublisher struct {
	observers []Observer
}

func (np *NewsPublisher) Attach(o Observer) {
	np.observers = append(np.observers, o)
}

func (np *NewsPublisher) Notify(news string) {
	for _, observer := range np.observers {
		observer.Update(news)
	}
}

// Observadores concretos
type WebSubscriber struct{ Name string }

func (w *WebSubscriber) Update(news string) {
	fmt.Printf("WEB [%s]: %s\n", w.Name, news)
}

type TVSubscriber struct{ Name string }

func (tv *TVSubscriber) Update(news string) {
	fmt.Printf("TV [%s]: Breaking News! %s\n", tv.Name, news)
}

type MobileSubscriber struct{ Name string }

func (m *MobileSubscriber) Update(news string) {
	fmt.Printf("APP [%s]: 🔔 %s\n", m.Name, news)
}

// Simulación
func main() {
	publisher := &NewsPublisher{}

	web := &WebSubscriber{Name: "ufcespanol"}
	tv := &TVSubscriber{Name: "Canal 1"}
	app := &MobileSubscriber{Name: "NotiApp"}

	publisher.Attach(web)
	publisher.Attach(tv)
	publisher.Attach(app)

	// Reportero envía noticia
	publisher.Notify("UFC 317: Topuria vs. Oliveira Por El Cinturón De Peso Ligero.")
}
